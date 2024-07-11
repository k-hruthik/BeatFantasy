# MySQL Queries and Outputs

Welcome to my MySQL queries and outputs repository. This collection showcases various SQL queries and their outputs from a dataset related to sports analytics.

## Query List

### 1. Top 10 User Teams and Points

- **Description:** Retrieves the top 10 user teams based on their points.
- **SQL Code:**
  ```sql
  SELECT team_name, player_points AS points
  FROM player_points
  ORDER BY player_points DESC
  LIMIT 10;
-**Output**+-----------+--------+
| team_name | points |
+-----------+--------+
| ALK       |     90 |
| PSV       |     88 |
| ALK       |     68 |
| PSV       |     58 |
| ALK       |     54 |
| ALK       |     42 |
| PSV       |     41 |
| PSV       |     36 |
| ALK       |     32 |
| PSV       |     31 |
+-----------+--------+
10 rows in set (0.00 sec)
  


