# Лаба по контейнерам
## 0. Пример с лекции - push_back для vector. График: capacity и size от i (номера итерации).
```C++
#include <iostream>
#include <fstream>
#include <vector>


int main() {
    std::vector<int> v;
    std::ofstream f("0.csv", std::ios::out);
    for (int i = 0; i < 1024; i++) {
        v.push_back(i);
        if (i % 50 == 0) {
            unsigned int cap = v.capacity();
            unsigned int s = v.size();
            f << i << " " << cap << " " << s << "\n";
        }
    }
}
```
![Зависимость размеров вектора](0.png)
