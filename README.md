# pywhoami


#### Setup Minikube
```
:➜  minikube start --vm=true

:➜  minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured
```

#### configure some minikube addons
```
:➜  minikube addons enable metrics-server                                                                                                                                
🌟  The 'metrics-server' addon is enabled

:➜  minikube addons enable ingress
🌟  The 'ingress' addon is enabled

:➜  minikube addons list
|-----------------------------|----------|--------------|
|         ADDON NAME          | PROFILE  |    STATUS    |
|-----------------------------|----------|--------------|
| ambassador                  | minikube | disabled     |
| dashboard                   | minikube | disabled     |
| default-storageclass        | minikube | enabled ✅   |
| efk                         | minikube | disabled     |
| freshpod                    | minikube | disabled     |
| gcp-auth                    | minikube | disabled     |
| gvisor                      | minikube | disabled     |
| helm-tiller                 | minikube | disabled     |
| ingress                     | minikube | enabled ✅   |
| ingress-dns                 | minikube | disabled     |
| istio                       | minikube | disabled     |
| istio-provisioner           | minikube | disabled     |
| kubevirt                    | minikube | disabled     |
| logviewer                   | minikube | disabled     |
| metallb                     | minikube | disabled     |
| metrics-server              | minikube | enabled ✅   |
| nvidia-driver-installer     | minikube | disabled     |
| nvidia-gpu-device-plugin    | minikube | disabled     |
| olm                         | minikube | disabled     |
| pod-security-policy         | minikube | disabled     |
| registry                    | minikube | disabled     |
| registry-aliases            | minikube | disabled     |
| registry-creds              | minikube | disabled     |
| storage-provisioner         | minikube | enabled ✅   |
| storage-provisioner-gluster | minikube | disabled     |
|-----------------------------|----------|--------------|
```

#### Get minikube ip
```
:➜  minikube ip         
192.168.64.5
```

#### Deploy the app using skaffold
```
:➜  skaffold run
Generating tags...
 - rpeets/pywhoami -> rpeets/pywhoami:4553a2e
Checking cache...
 - rpeets/pywhoami: Found. Tagging
Tags used in deployment:
 - rpeets/pywhoami -> rpeets/pywhoami:cc0854b1ba395d31bee520c562a4f048c70c63fe550ab701ccb82c2be23f07b9
Starting deploy...
 - secret/pywhoami-secret created
 - service/pywhoami created
 - deployment.apps/pywhoami created
 - poddisruptionbudget.policy/pywhoami created
 - horizontalpodautoscaler.autoscaling/pywhoami created
 - ingress.extensions/pywhoami.example.com created
Waiting for deployments to stabilize...
 - deployment/pywhoami: waiting for rollout to finish: 0 of 1 updated replicas are available...
 - deployment/pywhoami is ready.
Deployments stabilized in 14.283685571s
You can also run [skaffold run --tail] to get the logs
```

#### Test HPA using hey tool.
```
:➜  hey -z 10m -q 10 -c 20 http://192.168.64.5
```
