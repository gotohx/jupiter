## PostgreSQL pseudo_encrypt 算法

官方 wiki： [pseudo_encrypt](https://wiki.postgresql.org/wiki/Pseudo_encrypt)   

代码实现
```C
#include "postgres.h"
#include "fmgr.h"
#include <math.h>

PG_FUNCTION_INFO_V1(simple_feistel_self_inverse);

Datum
simple_feistel_self_inverse(PG_FUNCTION_ARGS)
{
	int32 val = PG_GETARG_INT32(0);
	int32 l1 = (val >> 16) & 0xffff;
	int32 r1 = val & 0xffff;
	int32 l2, r2;
	int i;

	for (i = 0; i < 3; i++)
	{
		l2 = r1;
		/* round() is used to produce the same values as the
		   plpgsql implementation that does an SQL cast to INT */
		r2 = l1 ^ (int32)round((((1366*r1 + 150889) % 714025) / 714025.0) * 32767);
		l1 = l2;
		r1 = r2;
	}

	PG_RETURN_INT32((r1 << 16) + l1);
}
```
搜索关键词：梅森旋转、mt19937   
原理： [梅森旋转](https://liam.page/2018/01/12/Mersenne-twister/)   
