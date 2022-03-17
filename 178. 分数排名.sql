/*表: Scores

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| score       | decimal |
+-------------+---------+
Id是该表的主键。
该表的每一行都包含了一场比赛的分数。Score是一个有两位小数点的浮点值。
 

编写 SQL 查询对分数进行排序。排名按以下规则计算:

分数应按从高到低排列。
如果两个分数相等，那么两个分数的排名应该相同。
在排名相同的分数后，排名数应该是下一个连续的整数。换句话说，排名之间不应该有空缺的数字。
按 score 降序返回结果表。

查询结果格式如下所示。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rank-scores
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/

select score,
       dense_rank() over (order by Score desc) as "rank"
from Scores