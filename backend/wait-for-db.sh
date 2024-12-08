until nc -z db 5432; do
    echo "Aguardando o banco de dados na porta 5432..."
    sleep 2
done
echo "Banco de dados disponível! Iniciando o backend."
exec "$@"

chmod +x wait-for-db.sh