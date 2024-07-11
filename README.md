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
-**Output**# Team Points Table

| team_name | points |
|-----------|--------|
| ALK       | 90     |
| PSV       | 88     |
| ALK       | 68     |
| PSV       | 58     |
| ALK       | 54     |
| ALK       | 42     |
| PSV       | 41     |
| PSV       | 36     |
| ALK       | 32     |
| PSV       | 31     |
## Query 2: Average Number of Teams Created per User

- **Description:** Calculates the average number of teams created per user.
- **SQL Code:**
  ```sql
  SELECT AVG(team_count) AS average_teams_per_user
  FROM (
      SELECT COUNT(DISTINCT team_name) AS team_count
      FROM player_points
      GROUP BY player_name
  ) AS user_team_counts;
-**Output** # Average Teams per User

| average_teams_per_user |
|------------------------|
|                 1.0000 |
## Query 3: Percentage of Users by Number of Teams Created

- **Description:** Calculates the percentage of users based on the number of teams they have created.
- **SQL Code:**
  ```sql
  SELECT team_count, (COUNT(*) / (SELECT COUNT(DISTINCT player_name) FROM player_points) * 100) AS percentage_of_users
  FROM (
      SELECT player_name, COUNT(DISTINCT team_name) AS team_count
      FROM player_points
      GROUP BY player_name
  ) AS user_team_counts
  WHERE team_count <= 20
  GROUP BY team_count;
-**Output**# Team Count Statistics

| team_count | percentage_of_users |
|------------|---------------------|
|          1 |            100.0000 |
## Query 4: Percentage of Teams with Captains by Position (GK, DEF, MID, ST)

- **Description:** Calculates the percentage of teams that have captains by position.
- **SQL Code:**
  ```sql
  SELECT player_pos, (COUNT(*) / (SELECT COUNT(DISTINCT team_name) FROM player_points) * 100) AS percentage_of_teams
  FROM player_points
  WHERE player_pos IN ('GK', 'DEF', 'MID', 'ST')
  GROUP BY player_pos;
-**Output**# Player Position Statistics

| player_pos | percentage_of_teams |
|------------|---------------------|
| DEF        |            500.0000 |
| ST         |            250.0000 |
| MID        |            550.0000 |
| GK         |            100.0000 |

## Query 5: Percentage of Teams with Vice Captains by Team (ALK, PSV)

- **Description:** Calculates the percentage of teams that have vice captains for teams ALK and PSV.
- **SQL Code:**
  ```sql
  SELECT team_name, (COUNT(*) / (SELECT COUNT(DISTINCT team_name) FROM player_points) * 100) AS percentage_of_teams
  FROM player_points
  WHERE team_name IN ('ALK', 'PSV')
  GROUP BY team_name;
-**Output**# Team Percentage Statistics

| team_name | percentage_of_teams |
|-----------|---------------------|
| ALK       |            700.0000 |
| PSV       |            700.0000 |




