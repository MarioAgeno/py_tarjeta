/*
Script SQL para corregir datos mal ingresados en Tarjetas para menterner la Integridad
Ejecutar en el Management de SQL antes de migrar las Tarjetas
*/

-- Quitar Campos Null
update tjTarjetas set adicional=0 where adicional is null
update tjTarjetas set titulo=0 where titulo is null
update tjTarjetas set vencimiento='1900-01-01' where vencimiento is null


-- Corregir Codigos Postales
UPDATE tjTarjetas SET cp = RTRIM(cp)
UPDATE tjTarjetas SET cp = LTRIM(cp)
update tjTarjetas set cp = 5137 where cp is null
update tjTarjetas set cp = 5137 where cp = ' '
update tjTarjetas set cp = 5137 where cp = '55137'
update tjTarjetas set cp = 5137 where cp = '513.7'
update tjTarjetas set cp = 5137 where cp = '51437'
update tjTarjetas set cp = 5137 where cp = '   5137'
update tjTarjetas set cp = 5138 where cp = '    5138'
update tjTarjetas set cp = 2435 where cp = '24345'
SELECT cp, count(cp) FROM tjTarjetas group by cp

select tjTarjetas.* from tjTarjetas where id='107529004' -- where vencimiento is null