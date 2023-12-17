struct subset_node {
    int key;
    subset_node *left, *right;
};

bool init(subset_node **sn) {
    *sn = nullptr;
    return true;
}

bool insert(subset_node **sn, int k) {
    if (!(*sn)) {
        auto *tmp = new subset_node();
        tmp->key = k;
        tmp->left = tmp->right = nullptr;
        *sn = tmp;
        return true;
    }
    if ((*sn)->key == k) return false;
    if (k > (*sn)->key) return insert(&(*sn)->right, k);
    else return insert(&(*sn)->left, k);
    return true;
}

subset_node **most_left(subset_node **sn) {
    if (!sn) return nullptr;
    if (!(*sn)) return nullptr;
    if (!(*sn)->left) return sn;
    return most_left(&(*sn)->left);
}

subset_node **find_pointer(subset_node **sn, int k) {
    if (!sn) return nullptr;
    if ((*sn)->key == k) return sn;
    if ((*sn)->left && k < (*sn)->key) {
        return find_pointer(&(*sn)->left, k);
    }
    if ((*sn)->right && k > (*sn)->key) {
        return find_pointer(&(*sn)->right, k);
    }
    return nullptr;
}

unsigned int height(subset_node *sn) {
    if (sn == nullptr) return 0;
    return 1 + std::max(height(sn->left), height(sn->right));
}

bool remove(subset_node **sn, int k) {
    if (!(*sn)) return false;
    subset_node **elem_delete = find_pointer(sn, k);
    if (!(elem_delete) or !(*elem_delete)) return false;
    subset_node *left = (*elem_delete)->left;
    subset_node *right = (*elem_delete)->right;
    delete *elem_delete;
    if (right) {
        subset_node **m_left = most_left(&right->left);
        *elem_delete = right;
        if (m_left) {
            (*m_left)->left = left;
        } else {
            right->left = left;
        }
    } else {
        *elem_delete = left;
    }
    return true;
}


subset_node *find(subset_node *sn, int k) {
    if (!sn) return nullptr;
    if (sn->key == k) return sn;
    if (k > sn->key) return find(sn->right, k);
    else return find(sn->left, k);
    return nullptr;
}

unsigned int size(subset_node *sn) {
    if (!sn) return 0;
    return 1 + size(sn->left) + size(sn->right);
}


void destructor(subset_node *sn) {
    if (!sn) return;
    destructor(sn->left);
    destructor(sn->right);
    delete sn;
}

int *DFS(subset_node *sn) {
    if (!sn) return nullptr;
    int *left = DFS(sn->left);
    int *right = DFS(sn->right);
    int *out = new int[size(sn->left) + 1 + size(sn->right)];
    for (unsigned int i = 0; i < size(sn->left); i++) {
        out[i] = left[i];
    }
    out[size(sn->left)] = sn->key;
    for (unsigned int i = 0; i < size(sn->right); i++) {
        out[size(sn->left) + 1 + i] = right[i];
    }
    delete[] left;
    delete[] right;
    return out;
}
