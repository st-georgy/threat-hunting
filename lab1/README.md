# Системы аутентификации и защиты от несанкционированного доступа

Лабораторная работа №1

## Цель

Вывести информацию о системе

## Исходные данные

1.  ОС Windows 11
2.  RStudio Desktop
3.  WSL2
4.  Интерпретатор языка R 4.2.2

## План

1.  Выполнить команду uname -r
2.  Выполнить команду cat /proc/cpuinfo \| grep "model name"
3.  Выполнить команду journalctl -q -b \| tail -n 30

## Шаги

```{r}
```

1.  Сначала выполним команду uname -r для вывода информации о системе

```{bash}
uname -r
```

	5.10.102.1-microsoft-standard-WSL2


2\. Далее команда cat /proc/cpuinfo \| grep "model name" для вывода информации о процессоре, строки которой содержат "model name"

```{bash}
cat /proc/cpuinfo | grep "model name"
```
	
	model name  : Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz
	model name  : Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz
	model name  : Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz
	model name  : Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz
	model name  : Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz
	model name  : Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz
	model name  : Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz
	model name  : Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz

3\. Также выполним команду journalctl -q -b \| tail -n 30 для вывода последних 30 строк логов

```{bash}
journalctl | tail -n 30
```

	Mar 01 09:59:58 Georgy-VivoBook systemd[1544]: Listening on GnuPG cryptographic agent (ssh-agent emulation).
	Mar 01 09:59:58 Georgy-VivoBook systemd[1544]: Listening on GnuPG cryptographic agent and passphrase cache.
	Mar 01 09:59:58 Georgy-VivoBook systemd[1544]: Listening on debconf communication socket.
	Mar 01 09:59:58 Georgy-VivoBook systemd[1544]: Listening on REST API socket for snapd user session agent.
	Mar 01 09:59:58 Georgy-VivoBook systemd[1544]: Listening on D-Bus User Message Bus Socket.
	Mar 01 09:59:58 Georgy-VivoBook systemd[1544]: Reached target Sockets.
	Mar 01 09:59:58 Georgy-VivoBook systemd[1544]: Reached target Basic System.
	Mar 01 09:59:58 Georgy-VivoBook systemd[1544]: Reached target Main User Target.
	Mar 01 09:59:58 Georgy-VivoBook systemd[1544]: Startup finished in 89ms.
	Mar 01 09:59:58 Georgy-VivoBook systemd[1]: Started User Manager for UID 1000.
	Mar 01 09:59:58 Georgy-VivoBook systemd[1]: Started Session c1 of user st-georgy.
	Mar 01 10:00:17 Georgy-VivoBook sudo[1574]: st-georgy : TTY=pts/0 ; PWD=/home/st-georgy ; USER=root ; COMMAND=/usr/bin/bash
	Mar 01 10:00:17 Georgy-VivoBook sudo[1574]: pam_unix(sudo:session): session opened for user root by (uid=0)
	Mar 01 10:00:20 Georgy-VivoBook systemd[1]: systemd-timedated.service: Succeeded.
	Mar 01 10:00:28 Georgy-VivoBook systemd[1]: Reloading.
	Mar 01 10:04:50 Georgy-VivoBook dbus-daemon[239]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.12' (uid=0 pid=747 comm="/usr/lib/snapd/snapd ")
	Mar 01 10:04:50 Georgy-VivoBook systemd[1]: Starting Time &amp; Date Service...
	Mar 01 10:04:50 Georgy-VivoBook dbus-daemon[239]: [system] Successfully activated service 'org.freedesktop.timedate1'
	Mar 01 10:04:50 Georgy-VivoBook systemd[1]: Started Time &amp; Date Service.
	Mar 01 10:05:20 Georgy-VivoBook systemd[1]: systemd-timedated.service: Succeeded.
	Mar 01 10:09:24 Georgy-VivoBook systemd[1]: Starting Ubuntu Advantage Timer for running repeated jobs...
	Mar 01 10:09:25 Georgy-VivoBook systemd[1]: ua-timer.service: Succeeded.
	Mar 01 10:09:25 Georgy-VivoBook systemd[1]: Finished Ubuntu Advantage Timer for running repeated jobs.
	Mar 01 10:09:43 Georgy-VivoBook snapd[747]: devicemgr.go:1761: no NTP sync after 10m0s, trying auto-refresh anyway
	Mar 01 10:14:41 Georgy-VivoBook systemd[1]: Starting Cleanup of Temporary Directories...
	Mar 01 10:14:42 Georgy-VivoBook systemd[1]: systemd-tmpfiles-clean.service: Succeeded.
	Mar 01 10:14:42 Georgy-VivoBook systemd[1]: Finished Cleanup of Temporary Directories.
	Mar 01 10:17:01 Georgy-VivoBook CRON[1679]: pam_unix(cron:session): session opened for user root by (uid=0)
	Mar 01 10:17:01 Georgy-VivoBook CRON[1680]: (root) CMD (   cd / &amp;&amp; run-parts --report /etc/cron.hourly)
	Mar 01 10:17:01 Georgy-VivoBook CRON[1679]: pam_unix(cron:session): session closed for user root

## Оценка результата

В результате лабораторной работы мы получили основную информацию об ОС, процессоре и логи системы.

## Вывод

Таким образом, мы научились работать с базовыми командами Linux и получать информацию об операционной системе.
