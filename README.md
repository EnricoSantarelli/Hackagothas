# 🚨 Gotham City Police Department
This project was developed as part of an internal hackathon organized by the university entity [Dev. Community Mauá](https://github.com/Maua-Dev). The goal of the project is to practice back-end knowledge using Python and develop skills in the Clean architecture.

## 🔥Features

The application simulates a police incident management system. The system has three main entities: Criminal, Criminal Record and Crime. Users can create, read, update and delete the criminal records in the system, also there are routes get and create crimes.

## 🧑‍💻Technologies Used
- Python 
- FastAPI
- Visual Studio Code

## ⚙️Installation and Usage
To test the project, it is necessary to use FastAPI as the project is currently mocked.
To install and run the project on your local machine, follow these steps:

```bash
  git clone https://github.com/EnricoSantarelli/Hackagothas.git
  pip install fastapi
  uvicorn main:app
```

## 🗺️Available Routes

#### Return all the mocked criminal records
```http
  GET /get_all_criminal_records/
```

#### Return a criminal record
```http
  POST /get_criminal_record/
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `criminal_record_id` | `string` | **Required**. The criminal record identifier |

#### Return a list of crimes
```http
  POST /get_crimes_by_criminal_record_id/
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `criminal_record_id` | `string` | **Required**. The criminal record identifier |

#### Return a list of crimes
```http
  POST /get_crimes_by_criminal_record_id/
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `criminal_record_id` | `string` | **Required**. The criminal record identifier |

#### Create a crime
```http
  POST /create_crime/
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `crime_type` | `CRIME_TYPE` | **Required**. the crime type of the new crime |
| `date` | `int` | **Required**. The date that occurred the new crime |
| `crime_description` | `string` | **Required**. The description of how occurred the new crime |
| `responsible_criminal` | `Criminal` | **Required**. Who is the responsible of the new crime |
| `crime_region` | `REGION` | **Required**. Where occurred the new crime |
| `seriousness` | `SERIOUSNESS` | **Required**. How seriousness was the crime |

#### Create a criminal record
```http
  POST /create_criminal_record/
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `new_criminal_record_id` | `string` | **Required**. The new criminal record identifier |
| `new_criminal_owner` | `Criminal` | **Required**. The new criminal owner of the criminal record |
| `new_danger_score` | `int` | **Required**. The new danger score of the criminal |
| `new_is_arrested` | `bool` | **Required**. The new is arrested to indicate if the criminal is in a prison |
| `new_prison` | `PRISON` | The new prison of the criminal if he is arrested |

#### Update a criminal record
```http
  PUT /update_criminal_record/
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `criminal_record_id` | `string` | **Required**. The criminal record identifier that will be updated |
| `new_criminal_owner` | `Criminal` | **Required**. The new criminal owner of the criminal record |
| `new_danger_score` | `int` | **Required**. The new danger score of the criminal |
| `new_is_arrested` | `bool` | **Required**. The new is arrested to indicate if the criminal is in a prison |
| `new_prison` | `PRISON` | The new prison of the criminal if he is arrested |

#### Delete a criminal record
```http
  DELETE /delete_criminal_record/
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `criminal_record_id` | `string` | **Required**. The criminal record identifier |

## 🪞References

 - [Dev. Community Clean MSS Template](https://github.com/Maua-Dev/clean_mss_template)
 - [Example followed](https://github.com/JoaoVitorBranco/HackaBeckas2.0)
 - [Teacher](https://github.com/JoaoVitorBranco)


## 🧑‍🎨Authors

- [@EnricoSantarelli](https://github.com/EnricoSantarelli)
- [@AmorimBreno](https://github.com/AmorimBreno)
