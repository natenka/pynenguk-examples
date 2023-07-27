from datetime import datetime, date, timedelta
import time
import click


@click.command()
@click.option("--pomodoros_to_run", "-r", default=5, show_default=True)
@click.option("--work_minutes", "-w", default=25, show_default=True)
@click.option("--short_break", "-s", default=5, show_default=True)
@click.option("--long_break", "-l", default=30, show_default=True)
@click.option("--set_size", "-p", default=4, show_default=True)
def cli(pomodoros_to_run, work_minutes, short_break, long_break, set_size):
    session_stats = {"total": pomodoros_to_run, "done": 0, "todo": pomodoros_to_run}
    while session_stats["todo"] != 0:
        session_stats["todo"] -= 1
        session_stats["done"] += 1
        if session_stats["todo"]:
            print(
                f"Pomodoros done: {session_stats['done']}, TODO: {session_stats['todo']}"
            )
        else:
            print(f"Good job! All {session_stats['done']} pomodoros done!")

    click.clear()
    all_pomodoros = list(range(1, pomodoros_to_run + 1))
    pomodoro_sets = [
        all_pomodoros[idx : idx + set_size]
        for idx in range(0, len(all_pomodoros), set_size)
    ]
    for pomodoro_set in pomodoro_sets:
        for idx, pomodoro_num in enumerate(pomodoro_set, 1):
            click.secho("It's time to work!", fg="green", bold=True)
            click.secho(f"Pomodoro {pomodoro_num}", fg="green", bold=True)
            message = "Work"
            start = datetime.now().replace(microsecond=0)
            for second in range(1, work_minutes + 1):
                time.sleep(0.1)
                now = datetime.now().replace(microsecond=0)
                print(f"\r{message}: {now-start}", end="", flush=True)
            print()

            if pomodoro_num == set_size:
                print("#" * 40)
                print(f"Long break for {long_break} minutes")
                message = "Long break"
                start = datetime.now().replace(microsecond=0)
                for second in range(1, work_minutes + 1):
                    time.sleep(0.1)
                    now = datetime.now().replace(microsecond=0)
                    print(f"\r{message}: {now-start}", end="", flush=True)
                print()

                print("#" * 40)
                break
            if not pomodoro_num == pomodoro_set[-1]:
                print("#" * 40)
                click.secho(
                    f"Short break for {short_break} minutes", fg="red", bold=True
                )
                message = "Short break"
                start = datetime.now().replace(microsecond=0)
                for second in range(1, work_minutes + 1):
                    time.sleep(0.1)
                    now = datetime.now().replace(microsecond=0)
                    print(f"\r{message}: {now-start}", end="", flush=True)
                print()
                print("#" * 40)


if __name__ == "__main__":
    cli()
