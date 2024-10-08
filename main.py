import os
import requests
import json


def create_invoice(
    pr_details, invoice_endpoint, api_key, amount, currency, memo=None, order_id=None
):

    # Extract PR number from the ref
    pr_url = pr_details.get("pull_request", {}).get("html_url")
    source_branch = pr_details.get("pull_request", {}).get("head", {}).get("ref")
    repo_name = pr_details.get("repository", {}).get("full_name").replace("/", ":")

    # Convert merge date to a more human-readable format

    # Create a descriptive memo with emojis
    default_memo = (
        f"🔧 **GitHub Repository:** {repo_name}\n"
        f"🔗 **Pull Request URL:** <{pr_url}>\n\nrepo"
        "✨ Thank you for your contribution! 🎉"
    )

    # Invoice data
    invoice_data = {
        "amount": float(amount),
        "currency": currency,
        "memo": memo or default_memo,
        "is_public": True,
        "order_id": order_id or f"{repo_name}:{source_branch}",
    }

    # Headers with API key
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    # Sending POST request to the invoicing API
    response = requests.post(invoice_endpoint, json=invoice_data, headers=headers)

    # Check for success
    if response.status_code == 201:
        print("✅ Invoice created successfully!")
    else:
        print(
            f"❌ Failed to create invoice. Status code: {response.status_code}, Response: {response.text}"
        )


def get_pull_request_info():
    # Read the GitHub event path from the environment variable
    event_path = os.getenv("GITHUB_EVENT_PATH")

    if not event_path:
        print("GITHUB_EVENT_PATH is not set.")
        return

    try:
        # Load the event data from the JSON file
        with open(event_path, "r") as file:
            event_data = json.load(file)

    except FileNotFoundError:
        print(f"Event file not found at {event_path}.")
    except json.JSONDecodeError:
        print("Error decoding JSON from the event file.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return event_data


if __name__ == "__main__":
    api_token = os.environ.get("INPUT_APITOKEN")
    if not api_token:
        raise Exception("Missing INPUT_APITOKEN")

    order_id = os.environ.get("INPUT_ORDERID")
    memo = os.environ.get("INPUT_MEMO")
    amount = os.environ.get("INPUT_AMOUNT", 1)
    currency = os.environ.get("INPUT_CURRENCY", "usd")
    server = os.environ.get("INPUT_SERVER", "https://perk.exchange")

    pr_details = get_pull_request_info()

    create_invoice(
        pr_details,
        f"{server}/api/invoices",
        api_key=api_token,
        amount=amount,
        currency=currency,
        order_id=order_id,
        memo=memo,
    )
