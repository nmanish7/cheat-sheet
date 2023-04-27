## ps 
- *ps stands for **process status** and it's a command used in Linux and Unix system to display information about running processes.*
	- `ps aux` ***aux** option display a detailed list of all running prcesses, including those belonging to other users and those not attached to a terminal.*
	- `ef` *option displays a hierarchical tree view of all running processes, with each process and its children indented under its parent process.*
	- `l` *option displays a more detailed list of information for each process, including the user and group IDs, the process ID, CPU and memory usage, and more.*
	- `u` *this option displays information about the user who started each process, including the user ID, terminal, and start time.*

### ps command category
1. Process selection options
2. Process display format options
3. Process sorting options
4. Additional options

#### Process Selection Options
- *Process selection options are used to select which processes to display based on certain criteria such as `user, PID, command name and more`. Here are some commonly used process selection options:*
	-   `-U`: Select processes belonging to a specific user or user ID. (Real User)
	-   `-u`: Select processes belonging to a specific user name or user ID. (Effective User)
	-   `-p`: Select processes with a specific process ID (PID).
	-   `-t`: Select processes associated with a specific terminal.
	```shell
	# Display process belonging to user john
	ps -u john
	
	# Display only the process with specific PID
	ps -p <pid>
	
	# Display process associated with a specific terminal
	ps -t <terminal>	
	```
#### Process Display Format Options
- *These options allow you to customize the output format of the process information displayed by ps, `such as which columns to include, the width fo the columns, and more.` Most commonly used options in this category are:*
	- -   `u`: Displays a detailed output format that includes the user who owns the process, the process ID, CPU usage, memory usage, start time, and command that started the process.
	-   `f`: Displays the output in a tree-like format that shows the relationship between parent and child processes.
	-   `o`: Allows you to specify the output format of the ps command. You can use this option to customize the columns and fields that are displayed for each process.
	```shell
	# Display the process ID, Parent Process ID and Command Name of all running processes.
	ps -eo pid,ppid,cmd
	```

#### Process Sorting Options
- *Process sorting options, which allow you to sort the output of ps based on specific criteria, `such as PID, CPU usage or memory usage.` Most commonly used sorting options are:*
	-   `k, --sort`: Sorts the processes based on the key (field). --sort/k option is used to specify the sorting order for the displayed processes.
		- **Different sorting options are available:**
			-  `%cpu`: sort by CPU usage, from highest to lowest.
			-   `%mem`: sort by memory usage, from highest to lowest.
			-   `args`: sort by command line arguments.
			-   `etime`: sort by elapsed time since the process was started, oldest first.
			-   `etime, -pid`: sort by elapsed time since the process was started, newest first.
			-   `pid`: sort by process ID, from lowest to highest.
			-   `-pid`: sort by process ID, from highest to lowest.
			-   `ppid`: sort by parent process ID, from lowest to highest.
			-   `-ppid`: sort by parent process ID, from highest to lowest.
			-   `stime`: sort by start time, from oldest to newest.
			-   `time`: sort by accumulated CPU time, from highest to lowest.
			-   `-time`: sort by accumulated CPU time, from lowest to highest.
			-   `user`: sort by user name.
			
	```shell
	# command is displaying information about processes in a hierarchical tree format, sorted by process ID (pid) and its parent process ID (ppid) in ascending order
	ps jak -ppid,+pid
	ps ja --sort -ppid,+pid
	```

#### Additional Options
-   *other options that don't fit into the above categories, `such as options to show process trees or display extended information`.*
	- -   `e`: Displays information about all processes, regardless of whether they are associated with a terminal.
	-   `h`: Suppresses the display of column headers in the output.
	-   `a`: Displays information about all processes on the same terminal as the ps command.

		```shell
		# supress the column headers in the output
		ps h
		
		```

---

### ps options category

1. UNIX options (***UNiplexed Information Computing System***)
2. BSD options (***Berkeley Source Distribution***)
3. GNU long options (***GNU's Not Unix***)


#### Unix Options
- UNIX options are preceded by a dash (`-`) and are used on most UNIX systems.

| Option | Description                                                                                                                                                   |
|:------:| ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -a | Select all processes except both session leaders and processes not associated with a terminal.
| -A | Select all processes.  Identical to -e. |
| -e | Select all processes.  Identical to -A. |
| -d | Select all processes except session leaders. |
| -o \<format> | User-defined format.  format is a single argument in the form of a blank-separated or comma-separated list. Headers may be renamed (ps -o pid,ruser=RealUser -o comm=Command) as desired.  If all column headers are empty (ps -o pid= -o comm=) then the header line will not be output.  Column width will increase as needed for wide headers; this may be used to widen up columns such as WCHAN (ps -o pid,wchan=WIDE-WCHAN-COLUMN -o comm).  Explicit width control (ps opid, wchan:42=column_name_if_required,cmd) is offered too. Use multiple -o options when in doubt. PS_FORMAT environment variable can be used to set default. Identical to o. |
| -O \<format> | Like -o, but preloaded with some default columns.  Identical to -o pid,format,state,tname,time,command.
| -C \<cmdlist> | Select by command name.  This selects the processes whose executable name is given in cmdlist. |
| -f | Do full-format listing.  This option can be combined with many other UNIX-style options to add additional columns.  It also causes the command arguments to be printed.  When used with -L, the NLWP (number of threads) and LWP (thread ID) columns will be added. |
| -F | Extra full format. | 
| -g \<grplist> | Select by session OR by effective group name. |
| -G \<grplist> | Select by real group ID (RGID) or name. The real group ID identifies the group of the user who created the process. Real group ID means primary Group ID of the user.|
| -p \<pidlist> | Select by Process ID. Identical to p and --pid. |
| -s \<sessionlist> | Select by session ID.  This selects the processes with a session ID specified in sesslist. |
| -t \<ttylist> | Select by Teletypewriter(tty)[terminal]. |
| -u \<userlist> | Select by effective user ID (EUID) or name. Effective user ID describes the user whose file access permissions are used by the process.|
| -U \<userlist> | Select by real user ID (RUID) or name. Real user ID identifies ther user who created the process. | 
| -N | Select all processes except those that fulfill the specified conditions (negates the selection). |
| -q \<pidlist> | Select by PID (quick mode).  This selects the processes whose process ID numbers appear in pidlist. With this option ps reads the necessary info only for the pids listed in the pidlist and doesn't apply additional filtering rules.  The order of pids is unsorted and preserved.  No additional selection options, sorting and forest type listings are allowed in this mode.  Identical to q and --quick-pid. |
| -c | Show different scheduler information for the -l option. |
| -j | Jobs format. |
| -l | Long format.  The -y option is often useful with this. |
| -y | Do not show flags; show rss in place of addr.  This option can only be used with -l. |
| -M | Add a column of security data.  Identical to Z (for SELinux). |
| -H | Show process hierarchy (forest). |
| -w | Wide output.  Use this option twice for unlimited width.|
| -L | Show threads, possibly with LWP (thread ID:Light Weight Process ID) and NLWP  (number of threads:Number of Lightweight Processes) columns. |
| -m | Show threads after processes. |
| -T | Show threads, possibly with SPID column. |


- **Example Command**
	```shell
	ps -a
	ps -e
	ps -A
	ps -eo 
	ps -Ao pid,state,tty,comm
	ps -AO ppid
	ps -C sleep # Here sleep is the command
	ps -ef
	ps -eF
	ps -p <pid>
	ps -t tty5,tty3
	ps -t tty5,tty3 -o pid,user,tty,state,comm
	ps -o pid,user,group,egroup,rgroup,comm -G <Real Groupname>
	ps -o pid,user,group,rgroup,egroup,comm -g <Effective Groupname>
	ps -o pid,user,euser,ruser,comm -U <Real Username>
	ps -o pid,user,ruser,euser,comm -u <Effective Username>
	# Select by Session ID
	ps -o sid= -p <pid>
	ps -s <Session ID>
	ps -eL
	ps -L -p 90
	ps -eo pid,ppid,lwp,nlwp,user,tty,state,comm
		
	```
---

#### BSD Options
- BSD options do not require a dash and are used on BSD-based systems such as macOS.

|      Option       | Description                                                                                                                                                                                                         |
|:-----------------:| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|         a         | display all the processes on the system, including those not associated with a terminal of current user. If you want to see all the process for all users, you can use aux or ax.                                   |
|    o \<format>    | Specify user-defined format.  Identical to -o and --format.                                                                                                                                                         |
|    O \<format>    | format is preloaded o (overloaded).  The BSD O option can act like -O (user-defined output format with some common fields predefined) or can be used to specify sort order.                                         |
|         c         | Show the true command name.                                                                                                                                                                                         |
|         x         | list all processes owned by you or to list all processes when used together with the a option.                                                                                                                      |
|         r         | Restrict the selection to only running processes.                                                                                                                                                                   |
|   p \<pidlist>    | Select by process ID.  Identical to -p and --pid.                                                                                                                                                                   |
|   q \<pidlist>    | Select by process ID (quick mode).  Identical to -q and --quick-pid.                                                                                                                                                |
|   t \<ttylist>    | Select by tty.  Nearly identical to -t and --tty, but can also be used with an empty ttylist to indicate the terminal associated with ps.  Using the T option is considered cleaner  using t with an empty ttylist. |
|         T         | Select all processes associated with this terminal.  Identical to the t option without any argument.                                                                                                                |
|   U \<userlist>   | Select by effective user ID (EUID) or name. Identical to -u and --user.                                                                                                                                             |
| k \<specfication>           | Specify sorting order.  Sorting syntax is [+ \| -]key,[+ \| -]key[,...]. Identical to --sort.                                                                                                                       |
|         j         | BSD job control format.                                                                                                                                                                                             |
|         l         | Display BSD long format.                                                                                                                                                                                            |
|         s         | Display signal format.                                                                                                                                                                                              |
|         u         | Display user-oriented format.                                                                                                                                                                                       |
|         v         | Display virtual memory format.                                                                                                                                                                                      |
|         X         | Register format.                                                                                                                                                                                                    |
|         Z         | Add a column of security data.  Identical to -M (for SELinux).                                                                                                                                                      |
|         e         | Show the environment after the command.                                                                                                                                                                             |
|         f         | ASCII art process hierarchy (forest).                                                                                                                                                                               |
|         h         | No header.  (or, one header per screen in the BSD personality).                                                                                                                                                     |
|         n         | Numeric output for WCHAN and USER (including all types of UID and GID).                                                                                                                                             |
|         w         | Wide output.  Use this option twice for unlimited width.                                                                                                                                                            |
|         H         | Show threads as if they were processes.                                                                                                                                                                             |
|         m         | Show threads after processes.                                                                                                                                                                                       |
|         L         | List all format specifiers.                                                                                                                                                                                         |
|         V         | Print the procps-ng version.                                                                                                                                                                                        |
- **Example Command**
	```shell
	
	```

---

#### GNU Options
- GNU options are preceded by two dashes (`--`) and are used on GNU/Linux systems.

| Option                  | Description                                                                                                                                                                              |
|:----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| --deselect              | Select all processes except those that fulfill the specified conditions (negates the selection). Identical to -N.                                                                        |
| --Group \<grplist>      | Select by real group ID (RGID) or name.  Identical to -G.                                                                                                                                |
| --group \<grplist>      | Select by effective group ID (EGID) or name.  The -g option is often an alternative to --group.                                                                                          |
| --pid \<pidlist>        | Select by process ID.  Identical to -p and p.                                                                                                                                            |
| --ppid \<pidlist>       | Select by parent process ID.  This selects the processes with a parent process ID in pidlist.  That is,               it selects processes that are children of those listed in pidlist. |
| --quick-pid \<pidlist>  | Select by process ID (quick mode).  Identical to -q and q.                                                                                                                               |
| --sid \<sessionlist>    | Select by session ID.  Identical to -s.                                                                                                                                                  |
| --tty \<ttylist>        | Select by terminal.  Identical to -t and t.                                                                                                                                              |
| --User \<userlist>      | Select by real user ID (RUID) or name.  Identical to -U.                                                                                                                                 |
| --user \<userlist>      | Select by effective user ID (EUID) or name.  Identical to -u and U.                                                                                                                      |
| --context               | Display security context format (for SELinux).                                                                                                                                           |
| --format \<format>      | user-defined format.  Identical to -o and o.                                                                                                                                             |
| --cols \<n>             | Set screen width.                                                                                                                                                                        |
| --columns \<n>          | Set screen width.                                                                                                                                                                        |
| --cumulative            | Include some dead child process data (as a sum with the parent).                                                                                                                         |
| --forest                | ASCII art process tree.                                                                                                                                                                  |
| --headers               | Repeat header lines, one per page of output.                                                                                                                                             |
| --lines \<n>            | Set screen height.                                                                                                                                                                       |
| --no-headers            | Print no header line at all.  --no-heading is an alias for this option.                                                                                                                  |
| --rows \<n>             | Set screen height.                                                                                                                                                                       |
| --sort \<specification> | Specify sorting order.  Sorting syntax is [+ \| -]key,[+ \| -]key[,...].  Identical to k.  For example: ps jax --sort=uid,-ppid,+pid                                                     |
| --width \<n>            | Set screen width.                                                                                                                                                                        |
| --help \<section>       | Print a help message.  The section argument can be one of simple, list, output, threads, misc, or all.                                                                                   |
| --info                  | Print debugging info.                                                                                                                                                                    |
| --version               | Print the procps-ng version.                                                                                                                                                             |


---
### Process State

| CODE | STATE OF PROCESS |
| ----|---- |
| D | uninterruptible sleep (usually IO) |
| I | Idle kernel thread |
| R | running or runnable (on run queue) |
| S | interruptible sleep (waiting for an event to complete) |
| T | stopped by job control signal |
| t | stopped by debugger during the tracing |
| W | paging (not valid since the 2.6.xx kernel) |
| X | dead (should never be seen) |
| Z | defunct ("zombie") process, terminated but not reaped by its parent |


- For BSD formats and when the stat keyword is used, additional characters may be displayed:

| CODE | STATE OF PROCESS |
| ---|---- |
| < | high-priority (not nice to other users) |
| N | low-priority (nice to other users) |
| L | has pages locked into memory (for real-time and custom IO) |
| s | is a session leader |
| l | is multi-threaded (using CLONE_THREAD, like NPTL pthreads do) |
| \+ | is in the foreground process group |

---

### Terminology

 - ** RUID (Real User ID):** 
	- **Let's imagine that Doraemon is running a program on his computer.**
	- *His **RUID (Real User ID)** would be the user ID of the person who started the program, which is Doraemon in this case. The RUID would stay constant throughout the program's execution and would determine the permissions the program has to access files and other system resources.*
	- *The RUID is the user ID of the user who started the process. It remains constant throughout the lifetime of the process, and it determines the permissions the process has to access files and other system resources.*
		```shell
		# As Doraemon user I run command
		sleep 300

		# Searching for pid of the above sleep command
		ps aux | grep sleep | grep -v sleep
		## doraemon     25120  0.0  0.0 217096   852 pts/4    S+   17:05   0:00 sleep 300

		# Now view the euser,ruser,user and command by pid
		 ps -o euser,ruser,user,cmd -p 25120
		## EUSER      RUSER      USER       CMD
		## doraemon   doraemon   doraemon   sleep 300
		
		
		# To view the general EUID, EUSER we use below command
		ps -eo ruid,ruser,pid,comm
		```
		
<br>


-   **EUID (Effective User ID):** 
	-  **Let's imagine that Doraemon is running a program on his computer.**
	- *His **EUID (Effective User ID)** would be the user ID that the program is currently running under. If Doraemon is running the program as a normal user, then the EUID would be the same as the RUID. But, if Doraemon is running the program with elevated privileges (such as with the `sudo` command), then the EUID would be different from the RUID. The EUID determines the permissions the program has to execute certain system calls.*
	- *This is the user ID that the process is currently running under. It may be different from the process's real user ID (RUID) if the process is running with elevated privileges, such as when running as root or with the `sudo` command.*
		```shell
		# See the passwd command permission (SUID) 
		ls -l $(which passwd)
		## -rwsr-xr-x. 1 root root 33424 Feb  7  2022 /usr/bin/passwd
		
		# Run passwd command on Doraemon user shell
		passwd
		
		# Now copy the other pid of passwd command
		ps aux | grep passwd | grep -v grep
		## root       25061  0.0  0.4 320056  8600 pts/4    S+   17:02   0:00 passwd

		# Now view the euser,ruser,user and command by pid
		ps -o euser,ruser,user,cmd -p 25061
		## EUSER    RUSER      USER     CMD
		## root     doraemon   root     passwd

		# To view the general EUID, EUSER we use below command
		ps -eo euid,euser,pid,comm
		```

<br>

-   **RGID (Real Group ID):** 
	- RGID is the group ID of the user who started the process.
	-  In the context of Doraemon, let's say that Doraemon belongs to a group called "NobitaGang". When Doraemon runs a command, the RGID will be the group ID of the user who started the process, in this case, the "NobitaGang" group.
	-   The RGID remains constant throughout the lifetime of the process.
		```shell
		ps -eo rgid,rgroup,pid,comm
		```


<br>

-   **EGID (Effective Group ID):** 
	- -   The EGID is the group ID that the process is currently running under. It may be different from the process's real group ID (RGID) if the process is running with elevated privileges, such as when running as root or with the `sudo` command.
	-   In the context of Doraemon, let's say that Doraemon has access to certain files that are owned by a different group, say "GianGang". When Doraemon runs a command to access those files, the system will look at the effective group ID to determine if Doraemon has the necessary permissions to access those files. If Doraemon's EGID matches the "GianGang" group, then it will be allowed to access those files.
	-   The EGID can be changed during the lifetime of the process.
	- Suppose Alice is a member of two groups - "developers" and "testers". In a shell where she is not a member of any supplementary groups, her EGID will be the same as her primary group (likely "developers"). However, if she runs a command that requires membership in the "testers" group (e.g. using the `newgrp` command), her EGID will be changed to "testers" temporarily.

		```shell
		ps -eo egid,egroup,pid,comm
		```


