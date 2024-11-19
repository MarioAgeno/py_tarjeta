/*
Script SQL para corregir datos mal ingresados en Comercios para menterner la Integridad
Ejecutar en el Management de SQL antes de migrar los Comercios
*/
-- Corregir Tipos de IVA
UPDATE tjComercios SET iva = RTRIM(iva)
UPDATE tjComercios SET iva = LTRIM(iva)
update tjComercios set iva = 'RI' where iva = 'R.I'
update tjComercios set iva = 'RI' where iva = 'RI '
update tjComercios set iva = 'RI' where iva = ' RI'
update tjComercios set iva = 'RMT' where iva = 'M '
update tjComercios set iva = 'RMT' where iva = 'MON '
update tjComercios set iva = 'RMT' where iva = 'MT '
update tjComercios set iva = 'RMT' where iva = '-'
update tjComercios set iva = 'RMT' where iva = '0'
update tjComercios set iva = 'EXE' where iva = 'E'
update tjComercios set iva = 'EXE' where iva = 'EX '
update tjComercios set iva = 'RMT' where iva = 'MTB '
update tjComercios set iva = 'RMT' where iva = 'R.M '
update tjComercios set iva = 'RMT' where iva = ' RM'
update tjComercios set iva = 'RMT' where iva = 'RM'
SELECT [iva], count(iva)
  FROM [Tarjetas].[dbo].[tjComercios] group by iva


-- Corregir Actividades
update tjComercios set actividad = 3 where actividad is null 
SELECT actividad, count(actividad)
  FROM [Tarjetas].[dbo].[tjComercios] group by actividad

-- Corregir Codigos Postales
UPDATE tjComercios SET cp = RTRIM(cp)
UPDATE tjComercios SET cp = LTRIM(cp)
update tjComercios set cp = 5137 where cp is null
update tjComercios set cp = 5137 where cp = ' 5137'
update tjComercios set cp = 5137 where cp = '   5137'
update tjComercios set cp = 5138 where cp = '    5138'
SELECT cp, count(cp) FROM tjComercios group by cp


-- Corregir Sucursales inexistentes
UPDATE tjComercios SET sucursal = 1 where sucursal>4
SELECT * FROM tjComercios where sucursal>4


--SELECT * FROM tjComercios where id= 11039