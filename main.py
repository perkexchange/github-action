import os
import requests


def main():
    if "INPUT_CAMPAIGNSECRET" not in os.environ:
        raise Exception("Missing INPUT_CAMPAIGNSECRET")
    if "INPUT_USERID" not in os.environ:
        raise Exception("Missing INPUT_USERID")

    campaign_secret = os.environ["INPUT_CAMPAIGNSECRET"]
    user_id = os.environ["INPUT_USERID"]

    if "INPUT_AMOUNT" in os.environ:
        amount = os.environ["INPUT_AMOUNT"]
    else:
        amount = 1

    if "INPUT_PLATFORM" in os.environ:
        platform = os.environ["INPUT_PLATFORM"]
    else:
        platform = "github"

    if "INPUT_SERVER" in os.environ:
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
