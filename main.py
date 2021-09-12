import os
import requests


def main():
    campaign_secret = os.environ["INPUT_CAMPAIGNSECRET"]
    user_id = os.environ["INPUT_USERID"]
    platform = os.environ["INPUT_PLATFORM"]
    amount = os.environ["INPUT_AMOUNT"]
    server = os.environ["INPUT_SERVER"]

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
