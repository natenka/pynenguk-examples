from datetime import datetime, date, timedelta
import time
import sys

import click


def print_green(message):
    click.secho(message, fg="green", bold=True)


def print_red(message):
    click.secho(message, fg="red", bold=True)


def draw_line(symbol="#", length=40):
    print(symbol * length)


def run_timer_with_live_stdout_update(minutes, message):
    start = datetime.now().replace(microsecond=0)
    # for second in range(1, (minutes * 60) + 1):
    for second in range(1, minutes + 1):
        time.sleep(0.1)
        # time.sleep(1)
        now = datetime.now().replace(microsecond=0)
        print(f"\r{message}: {now-start}", end="", flush=True)
    print()


def take_a_short_break(short_break=5):
    draw_line()
    print_red(f"Short break for {short_break} minutes")
    run_timer_with_live_stdout_update(short_break, "Short break")
    draw_line()


def take_a_long_break(long_break=30):
    draw_line()
    print(f"Long break for {long_break} minutes")
    run_timer_with_live_stdout_update(long_break, "Long break")
    draw_line()


def sets_of_pomodoros(podomoros_todo, set_size):
    for idx in range(0, len(podomoros_todo), set_size):
        yield podomoros_todo[idx : idx + set_size]


def run_pomodoro(pomodoro_num, work_minutes=25):
    print_green("It's time to work!")
    print_green(f"Pomodoro {pomodoro_num}")
    run_timer_with_live_stdout_update(work_minutes, "Work")
    print_green(next(stats))


def run_pomodoro_set(
    pomodoro_set, work_minutes=25, short_break=5, long_break=30, set_size=4
):
    for idx, pomodoro_num in enumerate(pomodoro_set, 1):
        run_pomodoro(pomodoro_num, work_minutes)
        if pomodoro_num == set_size:
            take_a_long_break(long_break)
            break
        if not pomodoro_num == pomodoro_set[-1]:
            take_a_short_break(short_break)


def update_session_stats(session_stats):
    while session_stats["todo"] != 0:
        session_stats["todo"] -= 1
        session_stats["done"] += 1
        if session_stats["todo"]:
            yield f"Pomodoros done: {session_stats['done']}, TODO: {session_stats['todo']}"
        else:
            yield f"Good job! All {session_stats['done']} pomodoros done!"


@click.command()
@click.option("--pomodoros_to_run", "-r", default=5, show_default=True)
@click.option("--work_minutes", "-w", default=25, show_default=True)
@click.option("--short_break", "-s", default=5, show_default=True)
@click.option("--long_break", "-l", default=30, show_default=True)
@click.option("--set_size", "-p", default=4, show_default=True)
def cli(pomodoros_to_run, work_minutes, short_break, long_break, set_size):
    session_stats = {"total": pomodoros_to_run, "done": 0, "todo": pomodoros_to_run}
    click.clear()
    all_pomodoros = list(range(1, pomodoros_to_run + 1))
    pomodoro_sets = sets_of_pomodoros(all_pomodoros, set_size)
    for pomo_set in pomodoro_sets:
        run_pomodoro_set(pomo_set, work_minutes, short_break, long_break)


if __name__ == "__main__":
    cli()
