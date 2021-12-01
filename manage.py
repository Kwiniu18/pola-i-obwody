import click
from figures import Triangle, Rectangle, Circle

def printing(area, peri, type_of):
    if area: click.echo(f"area: {type_of.area()}")
    if peri: click.echo(f"perimeter: {type_of.perimeter()}")

@click.group()
def cli():
    pass

@cli.command(help="obliczanie prostokata lub kwadratu")
@click.option("-a", type=int, default=1, help="nalezy podac!")
@click.option("-b", type=int, default=1, help="nalezy podac!")
@click.option("-area", required=False, is_flag=True, help="Do obliczenia pola")
@click.option("-peri", required=False, is_flag=True, help="Do obliczenia obwodu")

def rectangle(area, peri, a, b):
    type_of = Rectangle(a, b)
    printing(area, peri, type_of)

@cli.command(help="obliczanie kola")
@click.option("-r", type=int, default=1, help="nalezy podac!")
@click.option("-area", required=False, is_flag=True, help="Do obliczenia pola")
@click.option("-peri", required=False, is_flag=True, help="Do obliczenia obwodu")

def circle(r,area,peri):
    type_of = Circle(r)
    printing(area, peri, type_of)


@cli.command(help="obliczanie trojkata")
@click.option("-a", type=int, default=1, help="nalezy podac!")
@click.option("-b", type=int, default=1, help="nalezy podac!")
@click.option("-c", type=int, default=1, help="nalezy podac!")
@click.option("-h", type=int, default=1, help="nalezy podac!")
@click.option("-area", required=False, is_flag=True, help="Do obliczenia pola")
@click.option("-peri", required=False, is_flag=True, help="Do obliczenia obwodu")

def triangle(a, b, c, h, area, peri):
    type_of = Triangle(a, b, c, h)
    printing(area, peri, type_of)


if __name__ == "__main__":
    cli()
