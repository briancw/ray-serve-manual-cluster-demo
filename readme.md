Start the head node with
```bash
ray start --head
```

Build a docker image with all necessary deps for running the application.
Start workers with
```bash
ray start --address ray-head-ip:port
```

Build a config file for the serve application with:
```bash
serve build app_file_name:application -o deploy_config.yaml
```

Deploy the application with
```bash
serve deploy deploy_config.yaml
```
