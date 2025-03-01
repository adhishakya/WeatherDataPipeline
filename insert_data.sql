INSERT INTO weather_data(
    `name`,
    temperature,
    weather_type,
    weather_description,
    pressure,
    humidity,
    response_timestamp
)
VALUES(
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s
);

