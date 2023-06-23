import dax
import sys

# Usage: python delete_session_xnat.py project_id subject_id session_id

# Positional arguments - Project,Subject,Session
if len(sys.argv) != 4:
    print("Please provide three arguments: Project Subject_ID Session_ID")
else:
    project_id = sys.argv[1]
    subject_id = sys.argv[2]
    session_id = sys.argv[3]

xnat = dax  .XnatUtils.get_interface()
session = xnat.get_experiment_path(project_id,subject_id,session_id)
session_obj = xnat.select(session)
session_obj.delete()
