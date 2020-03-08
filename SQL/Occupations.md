Problem: https://www.hackerrank.com/challenges/occupations/problem?h_r=next-challenge&h_v=zen

MySQL: 
``set @a=0, @b=0, @c=0, @d=0; 
select max(D), max(P), max(S), max(A) from(
    select case when Occupation='Doctor'    then (@a:=@a+1)
                when Occupation='Professor' then (@b:=@b+1)
                when Occupation='Singer'    then (@c:=@c+1)
                when Occupation='Actor'     then (@d:=@d+1) 
                end as row,
    if( Occupation='Doctor'   , Name, NULL) as D,
    if( Occupation='Professor', Name, NULL) as P,
    if( Occupation='Singer'   , Name, NULL) as S,
    if( Occupation='Actor'    , Name, NULL) as A
    from OCCUPATIONS order by Name
) temp group by row 
``
