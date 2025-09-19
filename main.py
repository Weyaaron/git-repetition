import subprocess
import time
from git import Repo
from random import randrange
import os
def init_empty_repo_in_tmp()->Repo:

    base_dir = f"/tmp/git-repetition{randrange(0,100)}/"
    os.mkdir(base_dir)

    with open(f"{base_dir}test.json", "w") as file:
        file.write("{}")

    repo = Repo.init(base_dir, bare=True)
    repo.create_head("main")
    repo.commit("main")
    return repo

class Task:
    def setup(self):
        pass

    def teardown(self):
        pass

    def check_for_teardown(self):
        pass

        # Todo: Do a temporary directory with setup!

class SwitchBranchTask(Task):
    def __init__(self):
        self.target_branch_name = "Test"
        self.waiting_delay = 5

    def setup(self):
        status = subprocess.run(
            ["git", "branch", "--show-current"], capture_output=True
        )

    def display_command(self):
        print(
            f"Please switch to the branch '{self.target_branch_name}'. Create it if it does not exist."
        )

    def teardown(self):
        pass

    def check_for_teardown(self):
        status = subprocess.run(
            ["git", "branch", "--show-current"], capture_output=True, encoding="utf-8"
        )
        status_output = status.stdout.strip("\n")
        print(f"{status_output}, {self.target_branch_name}")
        return status_output == self.target_branch_name


def main():
    repo = init_empty_repo_in_tmp()
    print(repo.is_dirty())
    # first_task = SwitchBranchTask()
    # first_task.setup()
    # first_task.display_command()
    #
    # for i in range(0, 100):
    #     time.sleep(first_task.waiting_delay)
    #     check = first_task.check_for_teardown()
    #     print(f"Status:{check}, waited {i * first_task.waiting_delay} seconds")
    #     if check:
    #         exit()


if __name__ == "__main__":
    main()
