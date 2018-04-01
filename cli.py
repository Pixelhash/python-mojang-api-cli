#!/usr/bin/env python
import click
import requests
import datetime

USERNAME_TO_UUID = 'https://api.mojang.com/users/profiles/minecraft/{}'
UUID_TO_USERNAMES = 'https://api.mojang.com/user/profiles/{}/names'

HTTP_NO_CONTENT = 204


def uuid_add_dashes(uuid_str):
    return '-'.join([uuid_str[:8], uuid_str[8:12], uuid_str[12:16], uuid_str[16:20], uuid_str[20:]])


def timestamp_to_date(timestamp):
    return datetime.datetime.fromtimestamp(
        int(timestamp) / 1000
    ).strftime('%Y-%m-%d %H:%M:%S')


@click.group()
def main():
    """A simple script to make some basic calls to the Mojang API."""
    pass


@main.command()
@click.argument('username')
def uuid(username):
    """Looks up the UUID of a given username."""

    click.echo(f'Looking up UUID for username {username}')
    r = requests.get(USERNAME_TO_UUID.format(username))

    if r.status_code == HTTP_NO_CONTENT:
        click.echo('Username not found!')
    else:
        r_uuid = r.json()['id']
        click.echo(uuid_add_dashes(r_uuid))


@main.command()
@click.argument('uuid')
def username(uuid):
    """Looks up the usernames of a given UUID."""

    uuid = uuid.replace('-', '')

    click.echo(f'Looking up username for UUID {uuid}')
    r = requests.get(UUID_TO_USERNAMES.format(uuid))

    if r.status_code == HTTP_NO_CONTENT:
        click.echo('UUID not found!')
    else:
        r_json = r.json()
        original_name = r_json[0]['name']
        changed_names = r_json[1:]  # Skip first part to get only the changed usernames

        click.echo(f"Original username: {original_name}")

        for username_dict in changed_names:
            changed_name = username_dict['name']
            changed_at = timestamp_to_date(username_dict['changedToAt'])
            click.echo(f'Username: {changed_name}, Changed at: {changed_at}')


if __name__ == '__main__':
    main()
