import subprocess
returned_text = subprocess.check_output(&quot;speedtest-cli&quot;, shell=True,
universal_newlines=True)
print(&quot;The Result of Speed Test&quot;)
print(returned_text)