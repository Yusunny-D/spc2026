-- 1. non_usa_customers.sql: 
-- 미국에 거주하지 않는 고객(전체 이름, 고객 ID 및 국가)을 표시하는 쿼리를 제공합니다.
SELECT LastName ||" "|| FirstName AS FullName, CustomerId, Country 
	FROM customers WHERE Country != "USA";

-- 2. brazil_customers.sql: 
-- 브라질 고객만 표시하는 쿼리를 제공합니다.
SELECT * FROM customers WHERE Country="Brazil";

-- 3. brazil_customers_invoices.sql: 
-- 브라질 고객의 송장을 보여주는 쿼리를 제공합니다. 결과 테이블에는 고객의 전체 이름, 송장 ID, 송장 날짜 및 청구 국가가 표시되어야 합니다.
SELECT c.LastName ||" "|| c.FirstName AS FullName, i.invoiceId, i.invoiceDate, i.BillingCountry 
	From customers c 
		JOIN invoices i ON c.CustomerId = i.CustomerId
		WHERE c.Country = "Brazil"

-- 4. sales_agents.sql: 
-- 판매 대리인인 직원만 표시하는 쿼리를 제공하십시오.
SELECT * FROM employees WHERE title = 'Sales Support Agent';

-- 5. unique_invoice_countries.sql: 
-- 송장 테이블에서 청구 국가의 고유(unique)/고유(distinct) 목록을 표시하는 쿼리를 제공합니다.
SELECT DISTINCT BillingCountry FROM invoices;

-- 6. sales_agent_invoices.sql: 각 판매 에이전트와 연결된 송장을 표시하는 쿼리를 제공합니다. 
-- 결과 테이블에는 영업 에이전트의 전체 이름이 포함되어야 합니다.
SELECT e.lastname ||" "|| e.firstname as EmployeeFullName, i.* 
	FROM employees e 
		JOIN customers c ON c.SupportRepId = e.EmployeeId
		JOIN invoices i ON c.CustomerId = i.CustomerId;

-- 7. invoice_totals.sql: 모든 송장 및 고객에 대한 송장 합계, 고객 이름, 
-- 국가 및 판매 대리점 이름을 표시하는 쿼리를 제공합니다.
SELECT i.InvoiceId, i.Total, c.lastname ||" "|| c.firstname as CustomerFullName,
		i.BillingCountry, e.lastname ||" "|| e.firstname as EmployeeFullName
	FROM employees e 
		JOIN customers c ON c.SupportRepId = e.EmployeeId
		JOIN invoices i ON c.CustomerId = i.CustomerId;

-- 8. total_invoices_{year}.sql: 2009년과 2011년에 몇 개의 인보이스가 있었습니까?
SELECT COUNT(*) FROM invoices WHERE InvoiceDate BETWEEN '2009-01-01' AND '2011-12-31';

-- 9. total_sales_{year}.sql: 각 연도의 총 매출은 얼마입니까?
SELECT strftime('%Y', InvoiceDate) AS Year, SUM(Total) FROM invoices GROUP BY Year;

-- 10. invoice_37_line_item_count.sql: InvoiceLine 테이블을 보고 
-- Invoice ID 37에 대한 라인 항목 수를 계산하는 쿼리를 제공합니다.
SELECT BillingCountry, COUNT(*) FROM invoice_items WHERE invoiceid=37;

-- 11. line_items_per_invoice.sql: InvoiceLine 테이블을 보고 
-- 각 Invoice에 대한 라인 항목 수를 계산하는 쿼리를 제공합니다. 힌트: 그룹화 기준
SELECT invoiceid, BillingCountry, COUNT(*) FROM invoice_items GROUP BY invoiceid;

-- 12. line_item_track.sql: 각 송장 라인 항목에 구매한 트랙 이름을 포함하는 쿼리를 제공합니다.
SELECT i.*, t.Name
	FROM invoice_items i 
	JOIN tracks t ON i.TrackId = t.TrackId;

-- 13. line_item_track_artist.sql: 구매한 트랙 이름과 아티스트 이름을 포함하는 쿼리를 
-- 각 송장 라인 항목과 함께 제공합니다.
SELECT i.*, t.Name, ar.Name
	FROM invoice_items i 
	JOIN tracks t ON i.TrackId = t.TrackId
	JOIN albums al ON t.AlbumId = al.AlbumId
	JOIN artists ar ON al.ArtistId = ar.ArtistId;

-- 14. country_invoices.sql: 국가별 송장 수를 표시하는 쿼리를 제공합니다. 힌트: 그룹화 기준
SELECT BillingCountry, COUNT(*) FROM invoices GROUP BY BillingCountry;

-- 15. playlists_track_count.sql: 각 재생 목록의 총 트랙 수를 표시하는 쿼리를 제공합니다. 
-- 재생 목록 이름은 결과 테이블에 포함되어야 합니다.
SELECT pl.Name, COUNT(*)
	FROM playlist_track plt
	JOIN playlists pl ON pl.PlaylistId =plt.PlaylistId
	GROUP BY pl.Name;

-- 16. Tracks_no_id.sql: 모든 트랙을 표시하지만 ID는 표시하지 않는 쿼리를 제공합니다. 
-- 결과에는 앨범 이름, 미디어 유형 및 장르가 포함되어야 합니다.
SELECT t.Name, a.Title, m.Name, g.Name
	FROM tracks t
	JOIN albums a ON a.AlbumId = t.AlbumId
	JOIN media_types m ON m.MediaTypeId = t.MediaTypeId
	JOIN genres g ON g.GenreId = t.GenreId;

-- 17. invoices_line_item_count.sql: 모든 송장을 표시하지만 
-- 송장 라인 항목의 수를 포함하는 쿼리를 제공합니다.
SELECT *, COUNT(*) FROM invoice_items GROUP BY invoiceId;

-- 18. sales_agent_total_sales.sql: 판매 대리점별 총 매출을 조회하는 쿼리를 제공한다.
SELECT e.lastname ||" "|| e.firstname as EmployeeFullName, SUM(i.Total)
	FROM employees e 
		JOIN customers c ON c.SupportRepId = e.EmployeeId
		JOIN invoices i ON c.CustomerId = i.CustomerId
	WHERE e.Title = 'Sales Support Agent'
	GROUP BY EmployeeFullName;

-- 19. top_2009_agent.sql: 2009년 가장 많은 매출을 올린 판매원은?
--     힌트: 하위 쿼리에서 MAX 함수를 사용하십시오. 
SELECT EmployeeFullName, MAX(Total) 
FROM (SELECT e.lastname ||" "|| e.firstname as EmployeeFullName, SUM(i.Total) AS Total
	FROM employees e 
		JOIN customers c ON c.SupportRepId = e.EmployeeId
		JOIN invoices i ON c.CustomerId = i.CustomerId
	WHERE e.Title = 'Sales Support Agent' AND strftime('%Y', i.invoiceDate) = '2009'
	GROUP BY EmployeeFullName);

-- 20. top_agent.sql: 전체 판매 실적이 가장 많은 판매 대리점은?
SELECT EmployeeFullName, MAX(Total) 
FROM (SELECT e.lastname ||" "|| e.firstname as EmployeeFullName, SUM(i.Total) AS Total
	FROM employees e 
		JOIN customers c ON c.SupportRepId = e.EmployeeId
		JOIN invoices i ON c.CustomerId = i.CustomerId
	WHERE e.Title = 'Sales Support Agent'
	GROUP BY EmployeeFullName);

-- 21. sales_agent_customer_count.sql: 각 판매 대리점에 할당된 고객 수를 보여주는 쿼리를 제공한다.
SELECT e.lastname ||" "|| e.firstname as EmployeeFullName, COUNT(*)
FROM customers c
JOIN employees e ON c.SupportRepId = e.EmployeeId
WHERE e.Title = 'Sales Support Agent'
GROUP BY EmployeeFullName;

-- 22. sales_per_country.sql: 국가별 총 매출을 보여주는 쿼리를 제공한다.
SELECT BillingCountry, SUM(Total) From invoices GROUP BY BillingCountry;

-- 23. top_country.sql: 고객이 가장 많이 지출한 국가는 어디입니까?
SELECT BillingCountry, SUM(Total) AS CountryTotal From invoices 
GROUP BY BillingCountry ORDER BY CountryTotal DESC LIMIT 1;

-- 24. top_2013_track.sql: 2013년 가장 많이 구매한 트랙을 보여주는 쿼리를 제공합니다.
SELECT t.Name, COUNT(*) AS COUNT
FROM invoice_items it 
	JOIN tracks t ON it.TrackId = t.TrackId
	JOIN invoices i ON it.invoiceId = i.invoiceId
WHERE strftime('%Y', i.invoiceDate) = '2013'
GROUP BY t.Name
ORDER BY COUNT DESC
LIMIT 1;

-- 25. top_5_tracks.sql: 가장 많이 구매한 상위 5곡을 보여주는 쿼리를 제공합니다.
SELECT t.Name, COUNT(*) AS COUNT
FROM invoice_items it 
	JOIN tracks t ON it.TrackId = t.TrackId
	JOIN invoices i ON it.invoiceId = i.invoiceId
GROUP BY t.Name
ORDER BY COUNT DESC
LIMIT 5;

-- 26. top_3_artists.sql: 가장 많이 팔린 3명의 아티스트를 보여주는 쿼리를 제공합니다.
SELECT ar.Name, COUNT(*) AS COUNT
FROM invoice_items it 
	JOIN tracks t ON it.TrackId = t.TrackId
	JOIN albums al ON al.AlbumId = t.AlbumId
	JOIN artists ar ON ar.ArtistId = al.ArtistId
GROUP BY ar.Name
ORDER BY COUNT DESC
LIMIT 3;

-- 27. top_media_type.sql: 가장 많이 구매한 Media Type을 보여주는 쿼리를 제공한다.
SELECT m.Name, COUNT(*) AS COUNT
FROM invoice_items it 
	JOIN tracks t ON it.TrackId = t.TrackId
	JOIN media_types m ON m.MediaTypeId = t.MediaTypeId
GROUP BY m.MediaTypeId
ORDER BY COUNT DESC
LIMIT 1;