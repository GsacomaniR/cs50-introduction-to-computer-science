-- Primeiro, vamos verificar as tabelas disponíveis no banco de dados
.tables

-- Verificar a estrutura da tabela crime_scene_reports
.schema crime_scene_reports

-- Buscar o relatório da cena do crime em 28 de julho de 2023 na Fiftyville
SELECT * FROM crime_scene_reports
WHERE year = 2023 AND month = 7 AND day = 28 AND street = 'Fiftyville';

-- Resultado: O roubo ocorreu às 10:15am na Humphrey Street bakery.
-- Três testemunhas entrevistadas, cada uma mencionando a bakery.
-- Verificar entrevistas do dia seguinte
SELECT * FROM interviews
WHERE year = 2023 AND month = 7 AND day = 28;

-- Informações importantes das entrevistas:
-- Ruth: Dentro de 10 minutos do roubo, viu o ladrão entrar em um carro no estacionamento da bakery.
-- Verificar saídas do estacionamento entre 10:15 e 10:25

-- Eugene: Reconheceu o ladrão. Viu o ladrão usando o caixa eletrônico na Leggett Street antes do roubo.
-- Verificar transações no caixa eletrônico na Leggett Street na manhã de 28/07/2023

-- Raymond: Ao ligar para o cúmplice após o roubo, ouviu o cúmplice planejando pegar o voo mais cedo em 29/07/2023.
-- O cúmplice pediu para o ladrão comprar a passagem aérea.

-- Verificar saídas do estacionamento da bakery entre 10:15 e 10:25
.schema bakery_security_logs

SELECT * FROM bakery_security_logs
WHERE year = 2023 AND month = 7 AND day = 28
AND hour = 10 AND minute BETWEEN 15 AND 25
AND activity = 'exit';

-- Identificar possíveis carros (placas):
-- 5P2BI95, 94KL13X, 6P58WS2, 4328GD8, G412CB7, L93JTIZ, 322W7JE, 0NTHK55

-- Verificar transações no caixa eletrônico na Leggett Street
.schema atm_transactions

SELECT * FROM atm_transactions
WHERE year = 2023 AND month = 7 AND day = 28
AND atm_location = 'Leggett Street'
AND transaction_type = 'withdraw';

-- Identificar números de conta que fizeram saques

-- Verificar voos no dia 29/07/2023 (o mais cedo)
.schema flights
.schema airports

SELECT f.id, f.hour, f.minute, a1.full_name AS origin, a2.full_name AS destination
FROM flights f
JOIN airports a1 ON f.origin_airport_id = a1.id
JOIN airports a2 ON f.destination_airport_id = a2.id
WHERE f.year = 2023 AND f.month = 7 AND f.day = 29
ORDER BY f.hour, f.minute;

-- Voos mais cedo: ID 36 às 8:20 para Nova York (LaGuardia Airport)

-- Verificar passageiros do voo ID 36
.schema passengers

SELECT * FROM passengers WHERE flight_id = 36;

-- Identificar números de passaporte dos passageiros

-- Agora cruzar informações:
-- 1. Pessoas com carros que saíram da bakery (10:15-10:25)
-- 2. Que fizeram saque na Leggett Street na manhã de 28/07
-- 3. Que estavam no voo das 8:20 para Nova York em 29/07

-- Buscar pessoas que correspondem a todos os critérios
.schema people

SELECT p.name, p.phone_number, p.passport_number, p.license_plate,
       ba.account_number, pc.caller, pc.receiver
FROM people p
JOIN bakery_security_logs bsl ON p.license_plate = bsl.license_plate
JOIN bank_accounts ba ON p.id = ba.person_id
JOIN atm_transactions atm ON ba.account_number = atm.account_number
JOIN passengers ps ON p.passport_number = ps.passport_number
WHERE bsl.year = 2023 AND bsl.month = 7 AND bsl.day = 28
AND bsl.hour = 10 AND bsl.minute BETWEEN 15 AND 25
AND bsl.activity = 'exit'
AND atm.year = 2023 AND atm.month = 7 AND atm.day = 28
AND atm.atm_location = 'Leggett Street'
AND atm.transaction_type = 'withdraw'
AND ps.flight_id = 36;

-- Resultado: Bruce (telefone: (367) 555-5533, passaporte: 5773159633, placa: 94KL13X)

-- Verificar chamadas telefônicas de menos de 60 segundos em 28/07/2023
.schema phone_calls

SELECT * FROM phone_calls
WHERE year = 2023 AND month = 7 AND day = 28
AND duration < 60;

-- Verificar chamadas de Bruce (367) 555-5533
SELECT caller, receiver, duration FROM phone_calls
WHERE year = 2023 AND month = 7 AND day = 28
AND caller = '(367) 555-5533'
AND duration < 60;

-- Receptor: (375) 555-8161

-- Identificar o cúmplice (receptor da chamada)
SELECT name FROM people WHERE phone_number = '(375) 555-8161';

-- Resultado: Robin (cúmplice)

-- Confirmar cidade de fuga (destino do voo)
SELECT a.city FROM flights f
JOIN airports a ON f.destination_airport_id = a.id
WHERE f.id = 36;

-- Resultado: Nova York (New York City)
