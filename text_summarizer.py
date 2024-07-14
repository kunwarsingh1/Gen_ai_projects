import click
from transformers import pipeline


@click.command()
@click.argument('files', type=click.File('r',encoding='utf-8'), nargs=-1)
def cli(files):
    """Read file(s) part by part"""
    for file in files:
        data = (file.read())
        summarizer = pipeline("summarization")
        summary_text = summarizer(data,max_length=300,min_length=30,do_sample=False)
        click.echo(summary_text)



if __name__ == '__main__':
    cli()
