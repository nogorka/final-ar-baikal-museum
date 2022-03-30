INSERT INTO `Rooms` (`id`, `name`,`exsStr`) VALUES 
(1, 'Желтый зал', '1,2'),
(2, 'Синий зал', '3,4'),
(3, 'Зелёный зал', '5,6,7,8'),
(4, 'Общий зал', '9');

INSERT INTO `Entities` (`id`, `name`,`roomId`, `targetUri`, `overlayType`, `overlayUri`) VALUES 
(1, 'Экспонат 1', '1', 'assets/markers/zpt/1.zpt', 1, 'assets/overlays/1.mp4'),
(2, 'Экспонат 2', '1', 'assets/markers/zpt/2.zpt', 1, 'assets/overlays/2.mp4'),
(3, 'Экспонат 3', '2', 'assets/markers/zpt/3.zpt', 2, 'assets/overlays/3.jpg'),
(4, 'Экспонат 4', '2', 'assets/markers/zpt/4.zpt', 2, 'assets/overlays/4.jpg'),
(5, 'Экспонат 5', '3', 'assets/markers/zpt/5.zpt', 3, 'assets/overlays/5.glb'),
(6, 'Экспонат 6', '3', 'assets/markers/zpt/6.zpt', 3, 'assets/overlays/6.glb'),
(7, 'Экспонат 7', '3', 'assets/markers/zpt/7.zpt', 3, 'assets/overlays/7.glb'),
(8, 'Экспонат 8', '3', 'assets/markers/zpt/8.zpt', 3, 'assets/overlays/8.glb'),
(9, 'Сувенирная лавка', '4', 'assets/markers/zpt/9.zpt', 3, 'assets/overlays/9_1.glb');

INSERT INTO `Map` (`id`, `name`,`jsonUri`) VALUES (1, 'Музей капля Байкала', 'data/matrix.json');

INSERT INTO `PredefinedRoutes` (`id`, `name`,`route`, `mapId`) VALUES 
(1, 'Маршрут 1', '9,1,2,9,3,4,9,5,6,9', 1),
(2, 'Маршрут 2', '9,1,9,3,9,5', 1),
(3, 'Маршрут 3', '9,1,2,9', 1);
