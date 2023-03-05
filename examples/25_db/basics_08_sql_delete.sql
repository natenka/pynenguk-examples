
# 2022-12-15 06:44:13.077677
select * from switch
+----------------+----------+------------+-------------------+------------+-----------+
| mac            | hostname | model      | location          | mngmt_ip   | mngmt_vid |
+----------------+----------+------------+-------------------+------------+-----------+
| 0010.A1AA.C1CC | sw1      | Cisco 3750 | London, Green Str | <null>     | 255       |
| 0010.A1AA.21CC | sw101    | Cisco 3750 | London, Green Str | 10.1.1.101 | 255       |
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0030.A3AA.C3CC | sw3      | Cisco 3750 | London, Green Str | <null>     | 255       |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str | <null>     | 255       |
| 0070.A7AA.C7CC | sw7      | Cisco 3650 | London, Green Str | <null>     | 255       |
| 0110.A10A.C1CC | sw10     | 3750       | London, Green Str | <null>     | 255       |
+----------------+----------+------------+-------------------+------------+-----------+
9 rows in set
Time: 0.039s
Your call!

# 2022-12-15 06:44:52.597464
delete from switch where hostname = "sw10"
Query OK, 1 row affected
Time: 0.003s

# 2022-12-15 06:46:14.536572
quit
Goodbye!

# 2022-12-15 06:46:22.191047
select * from switch
+----------------+----------+------------+-------------------+------------+-----------+
| mac            | hostname | model      | location          | mngmt_ip   | mngmt_vid |
+----------------+----------+------------+-------------------+------------+-----------+
| 0010.A1AA.C1CC | sw1      | Cisco 3750 | London, Green Str | <null>     | 255       |
| 0010.A1AA.21CC | sw101    | Cisco 3750 | London, Green Str | 10.1.1.101 | 255       |
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0030.A3AA.C3CC | sw3      | Cisco 3750 | London, Green Str | <null>     | 255       |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str | <null>     | 255       |
| 0070.A7AA.C7CC | sw7      | Cisco 3650 | London, Green Str | <null>     | 255       |
| 0110.A10A.C1CC | sw10     | 3750       | London, Green Str | <null>     | 255       |
+----------------+----------+------------+-------------------+------------+-----------+
9 rows in set
Time: 0.037s
Your call!

# 2022-12-15 06:46:56.125135
delete from switch where hostname = "sw10"
Query OK, 1 row affected
Time: 0.003s

# 2022-12-15 06:46:59.895985
select * from switch
+----------------+----------+------------+-------------------+------------+-----------+
| mac            | hostname | model      | location          | mngmt_ip   | mngmt_vid |
+----------------+----------+------------+-------------------+------------+-----------+
| 0010.A1AA.C1CC | sw1      | Cisco 3750 | London, Green Str | <null>     | 255       |
| 0010.A1AA.21CC | sw101    | Cisco 3750 | London, Green Str | 10.1.1.101 | 255       |
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0030.A3AA.C3CC | sw3      | Cisco 3750 | London, Green Str | <null>     | 255       |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str | <null>     | 255       |
| 0070.A7AA.C7CC | sw7      | Cisco 3650 | London, Green Str | <null>     | 255       |
+----------------+----------+------------+-------------------+------------+-----------+
8 rows in set
Time: 0.025s

# 2022-12-15 06:47:11.785984
select * from switch
+----------------+----------+------------+-------------------+------------+-----------+
| mac            | hostname | model      | location          | mngmt_ip   | mngmt_vid |
+----------------+----------+------------+-------------------+------------+-----------+
| 0010.A1AA.C1CC | sw1      | Cisco 3750 | London, Green Str | <null>     | 255       |
| 0010.A1AA.21CC | sw101    | Cisco 3750 | London, Green Str | 10.1.1.101 | 255       |
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0030.A3AA.C3CC | sw3      | Cisco 3750 | London, Green Str | <null>     | 255       |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str | <null>     | 255       |
| 0070.A7AA.C7CC | sw7      | Cisco 3650 | London, Green Str | <null>     | 255       |
+----------------+----------+------------+-------------------+------------+-----------+
8 rows in set
Time: 0.019s
Your call!

# 2022-12-15 06:47:32.183527
delete from switch where hostname in ("sw1", "sw3")
Query OK, 2 rows affected
Time: 0.003s

# 2022-12-15 06:47:34.938458
select * from switch
+----------------+----------+------------+-------------------+------------+-----------+
| mac            | hostname | model      | location          | mngmt_ip   | mngmt_vid |
+----------------+----------+------------+-------------------+------------+-----------+
| 0010.A1AA.21CC | sw101    | Cisco 3750 | London, Green Str | 10.1.1.101 | 255       |
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str | <null>     | 255       |
| 0070.A7AA.C7CC | sw7      | Cisco 3650 | London, Green Str | <null>     | 255       |
+----------------+----------+------------+-------------------+------------+-----------+
6 rows in set
Time: 0.024s

# 2022-12-15 06:48:15.592069
select * from switch
+----------------+----------+------------+-------------------+------------+-----------+
| mac            | hostname | model      | location          | mngmt_ip   | mngmt_vid |
+----------------+----------+------------+-------------------+------------+-----------+
| 0010.A1AA.21CC | sw101    | Cisco 3750 | London, Green Str | 10.1.1.101 | 255       |
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str | <null>     | 255       |
| 0060.A6AA.C6CC | sw6      | C3750      | London, Green Str | <null>     | 255       |
| 0070.A7AA.C7CC | sw7      | Cisco 3650 | London, Green Str | <null>     | 255       |
+----------------+----------+------------+-------------------+------------+-----------+
6 rows in set
Time: 0.018s
Your call!

# 2022-12-15 06:48:57.788834
delete from switch where model like "%3750"
Query OK, 2 rows affected
Time: 0.003s

# 2022-12-15 06:48:59.606116
select * from switch
+----------------+----------+------------+-------------------+----------+-----------+
| mac            | hostname | model      | location          | mngmt_ip | mngmt_vid |
+----------------+----------+------------+-------------------+----------+-----------+
| 0020.A2AA.C2CC | sw2      | Cisco 3850 | London, Green Str | <null>   | 255       |
| 0040.A4AA.C4CC | sw4      | Cisco 3850 | London, Green Str | <null>   | 255       |
| 0050.A5AA.C5CC | sw5      | Cisco 3850 | London, Green Str | <null>   | 255       |
| 0070.A7AA.C7CC | sw7      | Cisco 3650 | London, Green Str | <null>   | 255       |
+----------------+----------+------------+-------------------+----------+-----------+
4 rows in set
Time: 0.021s

# 2022-12-15 06:50:36.705230
.exit
Goodbye!
