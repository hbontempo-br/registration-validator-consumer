import click
import requests
import json

from constants import URL, ADMINISTRATOR_EMAIL


@click.group()
def main():
    """
    Registration Validation Consumer- A small CLI made with a simple reason: consume hbontempo-br/register-validator-api (https://github.com/hbontempo-br/registration-validator-api)
    """
    click.echo(
        "A small CLI made with a simple reason: hbontempo-br/register-validator-api"
    )
    pass


@main.command()
@click.option("--debug", default=False)
def register(debug):
    """Register a new person"""

    click.echo("")
    click.echo("Please provide the person`s information.")

    body = {}
    body["first_name"] = input("First name: ")
    body["last_name"] = input("Last name: ")
    body["phone"] = input("Phone [format - (xx)xxxxxxxxx]: ")
    body["social_security_number"] = input("Social security number (only numbers): ")

    click.echo("")
    click.echo("Registering...")

    click.echo("")

    json_payload = json.dumps(body)
    headers = {"content-type": "application/json"}
    address = f"{URL}/registration"

    try:
        response = requests.post(url=address, data=json_payload, headers=headers)
    except requests.exceptions.ConnectionError as conn_ex:
        click.echo("Unable to connect to service. Please try again later")
        if debug:
            raise conn_ex
        return
    except Exception as ex:
        print(type(ex))
        return

    if response.status_code == 200:
        click.echo("Ok. Person registered.")
    elif response.status_code == 409:
        click.echo("A person with this social security number was already registered.")
    elif response.status_code == 400:
        response_body = json.loads(response.text)
        msg = response_body.get("msg")
        if msg:
            click.echo(f"Error. {msg}")
        else:
            click.echo(
                "Badly formatted information. Please check if the make sure "
                "the information was formatted correctly."
            )
    else:
        request_track_id = response.headers.get("request-track-id")
        click.echo("Error, something unexpected went wrong.", color="red")
        click.echo(
            f"Please contact the system administrator at {ADMINISTRATOR_EMAIL} "
            f"and provide the following information:"
        )
        click.echo(f"request-tracking-id: {request_track_id}")

    if debug:
        click.echo("")
        click.echo("")
        click.echo("### Debug ###")
        click.echo(f"Response status: {response.status_code}")
        click.echo(f"Response body: {response.text}")
        click.echo(f"Response headers: {response.headers}")


@main.command()
@click.argument("social_security_number")
@click.option("--debug", default=False)
def search(social_security_number, debug):
    """search new person through it`s social_security_number"""

    click.echo("")
    click.echo("Searching tor registration.")

    address = f"{URL}/registration/{social_security_number}"

    click.echo("")

    try:
        response = requests.get(url=address)
    except requests.exceptions.ConnectionError as conn_ex:
        click.echo("Unable to connect to service. Please try again later")
        if debug:
            raise conn_ex
        return
    except Exception as ex:
        print(type(ex))
        return

    if response.status_code == 200:
        click.echo("Person found.")
        response_body = json.loads(response.text)
        for key, value in response_body.items():
            click.echo(f"{key}: {value}")

    elif response.status_code == 404:
        click.echo("Person not registered")
    else:
        request_track_id = response.headers.get("request-track-id")
        click.echo("Error, something unexpected went wrong.", color="red")
        click.echo(
            f"Please contact the system administrator at {ADMINISTRATOR_EMAIL} "
            f"and provide the following information:"
        )
        click.echo(f"request-tracking-id: {request_track_id}")

    if debug:
        click.echo("")
        click.echo("")
        click.echo("### Debug ###")
        click.echo(f"Response status: {response.status_code}")
        click.echo(f"Response body: {response.text}")
        click.echo(f"Response headers: {response.headers}")


if __name__ == "__main__":
    main()
