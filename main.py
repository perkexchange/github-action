import os
import requests


def main():
    api_token = os.environ["INPUT_APITOKEN"]
    campaign_reference = os.environ["INPUT_CAMPAIGNREFERENCE"]
    user_id = os.environ["INPUT_USERID"]
    platform = os.environ["INPUT_PLATFORM"]
    amount = os.environ["INPUT_AMOUNT"]
    server = os.environ["INPUT_SERVER"]

    r = requests.post(
        "{}/api/campaigns/{}/reward".format(server, campaign_reference),
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Token {}".format(api_token),
        },
        json={
            "platform": platform,
            "user_id": user_id,
            "amount": float(amount),
        },
    )


if __name__ == "__main__":
    main()
