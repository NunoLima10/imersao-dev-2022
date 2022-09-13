const table_body = document.getElementById("table_body");
const api_url = "http://127.0.0.1:3000"

function CreateTeamRow(team){
    var table_row = document.createElement('TR');
    var team_name = document.createElement('TD');
    var games = document.createElement('TD');
    var victories = document.createElement('TD');
    var defeats = document.createElement('TD');
    var score = document.createElement('TD');

    table_row.id = team.id
    team_name.innerText = team.team_name;
    games.innerText = team.games;
    victories.innerText = team.victories;
    defeats.innerText = team.defeats;
    score.innerText = team.score;

    table_row.append(team_name);
    table_row.append(games);
    table_row.append(victories);
    table_row.append(defeats);
    table_row.append(score);

    return table_row;
}

function ShowTeams(team_list){
    for(let i=0 ; i <team_list.length; i++){
        table_row = CreateTeamRow(team_list[i])
        console.log(table_row)
        table_body.append(table_row)
    }
}

async function get_all_team(){
    let url = api_url + "/teams"
    const response =  await fetch(url)
    const data = await response.json()
    ShowTeams(data)
}

get_all_team()



































// async function get_text(){
//     const response =  await fetch(api_url)
//     const data = await response.json()
//     hello_text.innerText = data.data
    
// }



