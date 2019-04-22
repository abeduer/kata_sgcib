import click
from decimal import *

from app.account import Account
from app.client import Client


@click.command()
@click.argument('name')
@click.option('--balance', '-b')
def main(name, balance):
    if balance is None:
        balance = 0
    click.echo("Bonjour {}, Bienvenue au Kata SGCIB".format(name))
    account = Account(Decimal(balance))
    client = Client(name, account)
    click.echo("Votre solde est actuellement de : {} EUR".format(client.account.balance))
    if click.confirm('Voulez vous retirer de l\'argent?'):
        amount = click.prompt('Veuillez taper un montant correct', type=int)
        client.account.withdraw(amount)
        click.echo("Votre solde est désormais de : {} EUR".format(client.account.balance))
    click.echo("A bientôt !")


if __name__ == "__main__":
    main()
