def totalCasesByCountry():
    return """ SELECT  c.id_country country_code, c.name country_name, max(r. cumulative_cases) amount_cases
                FROM report r join country c on (r.id_country_country = c.id_country) 
                GROUP BY  c.id_country, c.name
                ORDER BY amount_cases DESC
            """
