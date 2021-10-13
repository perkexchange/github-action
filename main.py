import os
import requests


def main():
    if "INPUT_CAMPAIGNSECRET" in os.environ and os.environ["INPUT_CAMPAIGNSECRET"]:
        campaign_secret = os.environ["INPUT_CAMPAIGNSECRET"]
    else:
        raise Exception("Missing INPUT_CAMPAIGNSECRET")

    if "INPUT_USERID" in os.environ and os.environ["INPUT_USERID"]:
        user_id = os.environ["INPUT_USERID"]
    else:
        raise Exception("Missing INPUT_USERID")

    if "INPUT_AMOUNT" in os.environ and os.environ["INPUT_AMOUNT"]:
        amount = os.environ["INPUT_AMOUNT"]
    else:
        amount = 1

    if "INPUT_PLATFORM" in os.environ and os.environ["INPUT_PLATFORM"]:
        platform = os.environ["INPUT_PLATFORM"]
    else:
        platform = "github"

    if "INPUT_SERVER" in os.environ and os.environ["INPUT_SERVER"]:
        server = os.environ["INPUT_SERVER"]
    else:
        server = "https://perk.exchange"

    r = requests.post(
        "{}/api/rewards".format(server),
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Bearer {}".format(campaign_secret),
        },
        json={
            "platform": platform,
            "user_id": user_id,
            "amount": float(amount),
        },
    )


if __name__ == "__main__":
    main()
