from indeed import get_jobs
from save import save_to_file

jobs = get_jobs()
saved = save_to_file(jobs)