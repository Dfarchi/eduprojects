import subprocess

ret_val = subprocess.run(['ls', '-la'], capture_output=True)
# ret_val = subprocess.check_output(['ls', '-la'])
# print(ret_val)
print(ret_val.stdout)
# print(type(ret_val))
# print(ret_val.returncode)
# print(ret_val.args)