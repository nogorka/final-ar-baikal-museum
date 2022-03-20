INSERT INTO `Rooms` (`id`, `name`,`exsStr`) VALUES 
(1, 'Желтый зал', '1,2'),
(2, 'Синий зал', '3,4'),
(3, 'Зелёный зал', '5,6,7,8'),
(4, 'Общий зал', '9');

INSERT INTO `Entities` (`id`, `name`,`roomId`, `targetUri`, `overlayType`, `overlayUri`) VALUES 
(1, 'Экспонат 1', '1', 'None', 1, 'None'),
(2, 'Экспонат 2', '1', 'None', 1, 'None'),
(3, 'Экспонат 3', '2', 'None', 1, 'None'),
(4, 'Экспонат 4', '2', 'None', 1, 'None'),
(5, 'Экспонат 5', '3', 'None', 1, 'None'),
(6, 'Экспонат 6', '3', 'None', 1, 'None'),
(7, 'Экспонат 7', '3', 'None', 1, 'None'),
(8, 'Экспонат 8', '3', 'None', 1, 'None'),
(9, 'Сувенирная лавка', '4', 'None', 0, 'None');

INSERT INTO `Map` (`id`, `name`,`jsonUri`) VALUES (1, 'Музей капля Байкала', 'data/matrix.json');

INSERT INTO `PredefinedRoutes` (`id`, `name`,`route`, `mapId`) VALUES 
(1, 'Маршрут 1', '9,1,2,9,3,4,9,5,6,9', 1),
(2, 'Маршрут 2', '9,1,9,3,9,5', 1),
(3, 'Маршрут 3', '9,1,2,9', 1);
