persona = {
	"nombre":"Ruth",
  "apellidos":"Sainz Santos-Olmo",
  "correo":"info@jocarsa.com",
  "edad":18,
  "telefonos":[
  	{	
      "tipo":"fijo",
    	"numero":96123455
    },
    {	
      "tipo":"movil",
    	"número":65456546
    }
  ]
}

print(persona)
print(persona["telefonos"][0]["numero"])