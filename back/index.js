import express as 'express'
import cors as 'cors'

const app = express();

const {Client, Pool} = pg;

const pool = new Pool({
	user:"gilson",
	password:"admin",
	database:"alunos",
	port:5432,
	host:"localhost",
});

app.use(express.json())
app.use(cors())

app.get('/servidor.czgqkmic2jv4.us-east-2.rds.amazonaws.com',(req,res)=>{

})
app.post('/servidor.czgqkmic2jv4.us-east-2.rds.amazonaws.com',(req,res)=>{
	
})