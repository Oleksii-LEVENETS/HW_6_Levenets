# HW_6_Levenets
Hillel. Python Basic.
====================
ДЗ 6. HW_6
Створено: 21.12.2022 17:11
Заняття 13. Ітератор, генератор, корутина
-----------------------------------------
Task_1
1. Напишіть ітератор який приймає додатнє число n і видає всі числа фібоначі від 0 до n 
(якщо число більше чим n то воно не повертається). Добавте метод який перевіряє чи поточний стан ітератора – 
парне число.
-----------------------------------------
Task_2
1. Напишіть генератор який приймає число d (фіксована різниця між членами арифметичної прогресії) 
і кожним викликом next даний генератор повертає наступний член арифметичної прогресії.

2. Напишіть нескінченний генератор ідентифікаторів, ID створюється по шаблону “{prefix}-{number}”.
Де prefix – рядок що отримується від користувача, а number – інкремент.
Приклад використання – в генератор передається префікс ID, генератор при кожному звернені повертає
ID-1
ID-2
ID-3
якщо префікс INTERNAL-ID INTERNAL-ID-1 INTERNAL-ID-2 INTERNAL-ID-3
і тд.
Якщо префікс не передається то повертати потрібно тільки інкремент
1
2
3
Генератор завжди повертає тип даних string!
-----------------------------------------
Task_3
1. Напишіть корутину яка через метод send() отримує певне число, а повертає середнє арифметичне
чисел що були отримані раніше (включаючи те що отримали).
-----------------------------------------
