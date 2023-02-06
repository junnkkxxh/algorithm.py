SQL 

* 정렬
    * 오름차순(작 -> 큰)
        SELECT * FROM 테이블명 ORDER BY 정렬할 컬럼 ASC;
    * 내림차순(큰 -> 작)
        SELECT * FROM 테이블명 ORDER BY 정렬할 컬럼 DESC;
    * ORDER BY 다중 정렬일 경우, 왼쪽부터 순차적으로 정렬되기 때문에 순서를 고려해야 한다. 
        SELECT * FROM 테이블명 ORDER BY 정렬할 컬럼 DESC , 정렬할 컬럼 ASC;

* WHERE
    * WHERE 조건1(ex. user_id != 3) OR 조건2 AND 조건3;
    * WHERE user_id IN (1, 2);
        -> IN 연산자는 조건의 범위를 지정하는 데 사용. 이 값 중 하나 이상과 일치하면 조건에 맞는 것으로 평가 


* LIMIT
    * SELECT * FROM 테이블명 LIMIT 5; -> 5개 가져오기
    * 시작점(0부터 시작), 개수 지정
        SELECT * FROM 테이블명 LIMIT 5, 10; -> 6번째부터 10개 추출


* MAX/MIN
    * SELECT MAX(DATETIME) FROM 테이블명;
    * SELECT MIN(DATETIME) FROM 테이블명;


* 열 개수
    * SELECT COUNT(*) AS count FROM information_schema.columns WHERE table_name='테이블명';
* 행 개수
    * SELECT COUNT(*) FROM 테이블;


* DISTINCT 
    - 중복되는 데이터 제거를 위해 주로 Unique한 컬럼이나 tuple(record)를 조회하는 경우 사용. GROUP BY 보다 빠르다. 
    - DISTINCT -> 'Grouping’작업만, GROUP BY -> 'Grouping' + '정렬'
        * SELECT DISTINCT 컬럼명 FROM 테이블명;
        * SELECT COUNT(DISTINCT  컬럼명) FROM 테이블명;


* GROUP BY
    - 유형별로 갯수를 알고 싶을 때, 컬럼에 데이터를 그룹화 함.
        * 특정 컬럼을 그룹화하는 GROUP BY
            * 컬럼 그룹화 
                SELECT 컬럼 FROM 테이블명 GROUP BY 그룹화할 컬럼;
            * 조건 처리후 컬럼 그룹화
                SELECT 컬럼 FROM 테이블명 WHERE 조건식 GROUP BY 그룹화할 컬럼;
        * 특정 컬럼을 그룹화한 결과에 조건을 거는 HAVING (!= WHERE)
            * 컬럼 그룹화 후에 조건 처리
                SELECT 컬럼 FROM 테이블명 GROUP BY 그룹화할 컬럼 HAVING 조건식;
            * 조건 처리 후에 컬럼 그룹화 후에 조건 처리
                SELECT 컬럼 FROM 테이블명 WHERE 조건식 GROUP BY 그룹화할 컬럼 HAVING 조건식;
            * ORDER BY 가 존재하는 경우
                SELECT 컬럼 FROM 테이블명 [WHERE 조건식] GROUP BY 그룹화할 컬럼 [HAVING 조건식] ORDER BY 컬럼1 [, 컬럼2, 컬럼3, …];


* WHERE vs HAVING
    * WHERE
        SELECT * FROM 테이블명 WHERE 조건절
        - 항상 FROM 뒤에 위치 
        - 우선적으로 모든 필드에 조건을 둘 수 있음
    * HAVING 
        SELECT * FROM 테이블명 GROUP BY 필드명 HAVING 조건절
        - 항상 GROUP BY 뒤에 위치 
        - group by 된 후의 특정한 필드로 그룹화 되어진 새로운 테이블에 조건을 줄 수 있음
        
    * 예시
    1) select name, count(*) as cnt from where name='홍길동' 테이블 group by name; 
    2) select name, count(*) as cnt from 테이블 group by name having count(*)>1;


* JOIN
    * INNER JOIN
        * SELECT A.ID FROM A INNER JOIN B ON A.ID=B.ID;
    * LEFT JOIN
        * SELECT A.ID FROM A LEFT JOIN B ON A.ID=B.ID;
    * LEFT JOIN( IS NULL) 
        * SELECT A.ID FROM A LEFT JOIN B ON A.ID=B.ID WHERE B.ID IS NULL;
    * Outer -> Left & Right
        * SELECT A.ID FROM A LEFT INNER JOIN B ON A.ID=B.ID UNIONSELECT A.ID FROM A RIGHT INNER JOIN B ON A.ID=B.IDORDER BY A.ID;


* SET @변수명 := 값;
    -> 로컬 변수 설정

* BETWEEN a AND B : a, a+1, a+2, …, b까지

* HOUR(DATETIME) / MONTH(DATETIME)

* IFNULL(컬럼명, NULL 시 값)

* IS NULL / IS NOT NULL

* LIKE 
    * 특정 문자열로 시작
        SELECT [필드명] FROM [테이블명] WHERE [필드명] LIKE '특정 문자열%';
    * 특정 문자열로 끝
        SELECT [필드명] FROM [테이블명] WHERE [필드명] LIKE '%특정 문자열';
    * 특정 문자열 포함
        SELECT [필드명] FROM [테이블명] WHERE [필드명] LIKE '%특정 문자열%';
    * 복수 개의 특정 문자 포함
        SELECT [필드명] FROM [테이블명] WHERE [필드명] LIKE '%특정 문자열%' OR [필드명] LIKE '%특정 문자열2%';
        = 
        SELECT [필드명] FROM [테이블명] WHERE [필드명] REGEXP '특정 문자열|특정 문자열2';

* SQL 문
    - case : case 문 시작 
    - when : 필터링 할 조건을 기술 
    - then : 조건에 걸린 후 처리
    - else : 나머지 
    - end : case의 종료를 알림
        ex) select code,
                case
                    when code = 0
                        then '사료'
                    when code = 1
                        then '간식'
                    else 'ETC'
                    end as 상품카테고리
            from table
￼

* SQL REPLACE 문
    select code, replace(replace(replace(replace(code, '0', '사료'), '1', '간식'), '2', '영양제'), '3', '용품') as 상품 카테고리 from table;

* IF(조건문, TRUE, FALSE)
    ex) SELECT ANIMAL_ID, NAME, 
	     IF((SEX_UPON_INTAKE LIKE "Neutered%") OR (SEX_UPON_INTAKE LIKE "Spayed%"), "O", "X")  AS "중성화" 
	    FROM ANIMAL_INS;

* DATE_FORMAT(DATETIME, '%Y-%m-%d')


* 숫자
    * CEIL -> 올림 
        CEIL(0.12) — 1
        
    * ROUND -> 반올림 
        ROUND(0.512) — 1
        ROUND(0.512, 2) — 0.57 (반올림 자릿수 설정)

    * FLOOR , TRUNCATE -> 버림 
        FLOOR(0.911) — 0
        TRUNCATE(0.21, 1) — 0.2

    * ABS -> 절댓값
        ABS(100) — 100
        ABS(-100) — 100

    * POW -> 제곱
        POW(10,2) — 100

    * MOD -> 나머지 
        MOD(10,3) — 1

    * GREATEST -> 최댓값
        GREATEST(10, 4, 20, 1) — 20

    * LEAST -> 최솟값
        LEAST(10, 4, 20, 1) — 1
