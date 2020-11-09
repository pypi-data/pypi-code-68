"""Menu item that provides detailed information for a single job."""
import subprocess

from bullet import Bullet, colors
from getch import pause

from vigorish.cli.components import print_message
from vigorish.cli.menu_item import MenuItem
from vigorish.constants import EMOJI_DICT, MENU_NUMBERS
from vigorish.enums import JobStatus
from vigorish.scrape.job_runner import JobRunner
from vigorish.util.list_helpers import report_dict
from vigorish.util.result import Result


class JobDetailsMenuItem(MenuItem):
    def __init__(self, app, db_job, menu_item_number):
        super().__init__(app)
        self.db_job = db_job
        self.job_status = db_job.status
        self.job_details = db_job.job_details
        self.menu_item_text = f" {db_job.name} (Status: {db_job.status.name}, ID: {db_job.id})"
        self.menu_item_emoji = MENU_NUMBERS.get(menu_item_number, f"{menu_item_number}. ")
        self.exit_menu = False

    def launch(self):
        subprocess.run(["clear"])
        print_message("*** Job Details ***", fg="bright_yellow", bold=True)
        job_details = report_dict(self.job_details, title="", title_prefix="", title_suffix="")
        print_message(f"{job_details}\n", wrap=False, fg="bright_yellow")
        if self.db_job.errors:
            print_message("*** Errors ***", fg="bright_red", bold=True)
            print_message(self.db_job.error_messages, fg="bright_red")
        if self.job_status == JobStatus.INCOMPLETE:
            result = self.incomplete_job_options_prompt()
            if result.failure:
                return Result.Ok(self.exit_menu)
            user_choice = result.value
            if user_choice == "RUN":
                job_runner = JobRunner(
                    db_job=self.db_job,
                    db_session=self.db_session,
                    config=self.config,
                    scraped_data=self.scraped_data,
                )
                result = job_runner.execute()
                if result.failure:
                    return result
                return Result.Ok(True)
            if user_choice == "CANCEL":
                self.db_job.status = JobStatus.COMPLETE
                self.db_session.commit()
                subprocess.run(["clear"])
                print_message("Job was successfully cancelled.", fg="bright_red", bold=True)
                pause(message="Press any key to continue...")
                return Result.Ok(True)
        if self.job_status == JobStatus.ERROR:
            result = self.failed_job_options_prompt()
            if result.failure:
                return Result.Ok(self.exit_menu)
            user_choice = result.value
            if user_choice == "RETRY":
                job_runner = JobRunner(
                    db_job=self.db_job,
                    db_session=self.db_session,
                    config=self.config,
                    scraped_data=self.scraped_data,
                )
                result = job_runner.execute()
                if result.failure:
                    return result
                return Result.Ok(True)
        else:
            pause(message="\nPress any key to return to the previous menu...")
            return Result.Ok(self.exit_menu)

    def incomplete_job_options_prompt(self):
        choices = {
            f"{MENU_NUMBERS.get(1)}  Execute Job": "RUN",
            f"{MENU_NUMBERS.get(2)}  Cancel Job": "CANCEL",
            f"{EMOJI_DICT.get('BACK')} Return to Incomplete Jobs": None,
        }
        prompt = Bullet(
            "Current options:",
            choices=[choice for choice in choices.keys()],
            bullet="",
            shift=1,
            indent=2,
            margin=2,
            bullet_color=colors.foreground["default"],
            background_color=colors.foreground["default"],
            background_on_switch=colors.foreground["default"],
            word_color=colors.foreground["default"],
            word_on_switch=colors.bright(colors.foreground["cyan"]),
        )
        choice_text = prompt.launch()
        choice_value = choices.get(choice_text)
        return Result.Ok(choice_value) if choice_value else Result.Fail("")

    def failed_job_options_prompt(self):
        choices = {
            f"{MENU_NUMBERS.get(1)}  Retry Job": "RETRY",
            f"{EMOJI_DICT.get('BACK')} Return to Failed Jobs": None,
        }
        prompt = Bullet(
            "Current options:",
            choices=[choice for choice in choices.keys()],
            bullet="",
            shift=1,
            indent=2,
            margin=2,
            bullet_color=colors.foreground["default"],
            background_color=colors.foreground["default"],
            background_on_switch=colors.foreground["default"],
            word_color=colors.foreground["default"],
            word_on_switch=colors.bright(colors.foreground["cyan"]),
        )
        choice_text = prompt.launch()
        choice_value = choices.get(choice_text)
        return Result.Ok(choice_value) if choice_value else Result.Fail("")
