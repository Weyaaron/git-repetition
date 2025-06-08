import subprocess
import time


class Task:
    def setup(self):
        pass

    def teardown(self):
        pass

    def check_for_teardown(self):
        pass


class SwitchBranchTask(Task):
    def __init__(self):
        self.target_branch_name = "Test"

    def setup(self):
        status = subprocess.run(
            ["git", "branch", "--show-current"], capture_output=True
        )
        # CompletedProcess(args=['ls', '-l', '/dev/null'], returncode=0,
        # stdout=b'crw-rw-rw- 1 root root 1, 3 Jan 23 16:23 /dev/null\n', stderr=b'')
        pass

    def teardown(self):
        pass

    def check_for_teardown(self):
        status = subprocess.run(
            ["git", "branch", "--show-current"], capture_output=True, encoding="utf-8"
        )
        print(status.stdout)
        return status.stdout == self.target_branch_name


def main():
    first_task = SwitchBranchTask()
    first_task.setup()

    for i in range(100):
        time.sleep(1)
        check = first_task.check_for_teardown()
        print(f"Status:{check}, waited {i} seconds")
        if check:
            exit()


if __name__ == "__main__":
    main()
