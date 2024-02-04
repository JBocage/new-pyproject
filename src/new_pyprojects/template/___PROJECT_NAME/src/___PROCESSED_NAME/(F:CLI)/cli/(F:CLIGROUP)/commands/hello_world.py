import click


@click.command("hello-world")
@click.option(
    "--shout",
    "shout",
    is_flag=True,
    help="Shouts instead of speaking",
)
@click.pass_context
def hello_world(ctx, *args, **kwargs):
    """
    Hello world command
    """
    for key, value in kwargs.items():
        ctx.obj.set_config(key, value)

    args = ctx.obj.config

    # Do something
    if args.pop("shout"):
        print("HELLO WOOOORLD!")
    else:
        print("hello world")
