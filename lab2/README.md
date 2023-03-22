# Системы аутентификации и защиты от несанкционированного доступа

Лабораторная работа №2

## Цель

1.  Развить практические навыки использования современного стека инструментов сбора и аналитической обработки информации о сетвом трафике
2.  Освоить базовые подходы блокировки нежелательного сетевого трафика
3.  Закрепить знания о современных сетевых протоколах прикладного уровня

## Исходные данные

1.  ОС Windows 11
2.  WSL2
3.  Wireshark
4.  Zeek
5.  Python 3.10

## Задание

1.  Собрать сетевой трафик (объемом не менее 100 Мб)
2.  Выделить метаинформацию сетевого трафика с помощью утилиты Zeek
3.  Собрать данные об источниках нежелательного трафика, например -- <https://github.com/StevenBlack>
4.  Написать программу на любом удобном языке (python, bash, R ...), котрая подсчитывает процент нежелательного трафика в собранном на этапе 1.
5.  Оформить отчет в соответствии с шаблоном

## План

Работу целесообразно разделить на 2 этапа: сбора собственных данных и сбора данных о нежелательном трафике.

<img width="960" alt="wireshark" src="https://user-images.githubusercontent.com/83448561/226827205-16e8c4fb-1a60-43ce-ab85-fc719914f24b.png">

## Шаги

1\. Собрать сетевой трафик (объемом не менее 100 Мб) с помощью сетевого анализатора Wireshark

2\. Выделить метаинформацию сетевого трафика с помощью утилиты Zeek

Чтение PCAP:

    zeek –C –r traffic.pcapng

Команда для вычленения адресов из dns.log:

    awk '/^[^#]/ {print $10}' dns.log >> dns

Полученные файлы:

<img width="639" alt="files" src="https://user-images.githubusercontent.com/83448561/226827274-c1f01960-7f72-4ce8-84b1-f324bc3493ea.png">

3\. Собрать данные об источниках нежелательного трафика с github -- [https://github.com/StevenBlack/hosts/blob/master/data/KADhosts/hosts](https://github.com/StevenBlack/hosts/tree/master/data)

С репозитория взяты несколько файлов и объединенны в один файл hosts с помощью команды

    cat hosts2 >> hosts1

Вычленение из hosts1:

    cat hosts1 | cut -d " " -f2 >> hosts

4\. Написать программу на языке Python 3.10, которая подсчитывает процент нежелательного трафика в собранном на этапе 1:

Исходный код:

```{python}
def main():
	with open('dns', 'r') as dns, open('hosts', 'r') as hosts:
		dns_lines = dns.readlines()
		dns_lines = [line.strip() for line in dns_lines if line.strip() and line.strip() != "-"]
		hosts_lines = hosts.readlines()
		hosts_lines = [line.strip() for line in hosts_lines if line.strip() and line.strip() != "-" and line.strip() != "#"]
		dns_set = set(dns_lines)
		hosts_set = set(hosts_lines)
		common_lines = dns_set.intersection(hosts_set)

	dns_count = len(dns_lines)
	common_count = len(common_lines)
	percent = round(common_count / dns_count * 100, 2)
	print(f"Процент нежелательного трафика: {percent}%")

if __name__ == '__main__':
	main()
```

## Оценка результата

Собрано 100+ Мб трафика

Собраны данные об источниках нежелательного трафика

Проведенно их сравнение, найденны записи нежелательного трафика в нашем

Подсчитали процент нежелательного трафика

Получены результаты:

<img width="472" alt="percent" src="https://user-images.githubusercontent.com/83448561/226827292-7b863290-4ae7-4a8a-bc5b-ed6fdcbc3c54.png">

## Вывод

В результате выполнения работы были освоены основные инструменты сбора трафика через анализатор Wireshark, выделения информации о dns собранного трафика с помощью Zeek и анализа нежелательного трафика на Python.
