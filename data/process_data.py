import sys

sys.path.insert(0, '../')
# print(sys.path)
import config
from data_utils import (make_conll_format, make_embedding, make_vocab,
                        make_vocab_from_squad, process_file, process_txt_files)




def make_sent_dataset():
    train_src_file = "./para-train.txt"
    train_trg_file = "./tgt-train.txt"

    embedding_file = "./glove.840B.300d.txt"
    embedding = "./embedding.pkl"
    word2idx_file = "./word2idx.pkl"
    # make vocab file
    word2idx = make_vocab(train_src_file, train_trg_file, word2idx_file, config.vocab_size)
    make_embedding(embedding_file, embedding, word2idx)


def make_para_dataset():
    embedding_file = "../glove.840B.300d.txt"
    embedding = "./embedding.pkl"
    src_word2idx_file = "./word2idx.pkl"

    train_squad = "../squad/train-v1.1.json"
    # train_squad = "../squad/test.json"
    dev_squad = "../squad/dev-v1.1.json"
    # dev_squad = "../squad/test.json"
    # testtgt = '../test_tgt.txt'
    # testsrc = '../test_src.txt'
    # testans = '../test_ans.txt'
    # train_src_nqg = '../squad_nqg/para-train.txt'
    # train_tgt_nqg = '../squad_nqg/tgt-train.txt'
    # train_ans_nqg = '../squad_nqg/src-train.txt'

    # dev_src_nqg = '../squad_nqg/para-dev.txt'
    # dev_tgt_nqg = '../squad_nqg/tgt-dev.txt'
    # dev_ans_nqg = '../squad_nqg/src-dev.txt'

    # test_src_nqg = '../squad_nqg/para-test.txt'
    # test_tgt_nqg = '../squad_nqg/tgt-test.txt'
    # test_ans_nqg = '../squad_nqg/src-test.txt'

    train_src_file = "../squad/para-train.txt"
    train_trg_file = "../squad/tgt-train.txt"
    dev_src_file = "../squad/para-dev.txt"
    dev_trg_file = "../squad/tgt-dev.txt"

    test_src_file = "../squad/para-test.txt"
    test_trg_file = "../squad/tgt-test.txt"

    # pre-process training data
    train_examples, counter = process_file(train_squad)
    # train_examples, counter = process_txt_files(testsrc,testtgt,testans)
    # train_examples, counter = process_txt_files(train_src_nqg,train_tgt_nqg,train_ans_nqg)
    print('counter',len(counter))
    # print('trainexample',train_examples)
    # print('counter',counter)
    make_conll_format(train_examples, train_src_file, train_trg_file)
    word2idx = make_vocab_from_squad(src_word2idx_file, counter, config.vocab_size)
    # print('word2idx',word2idx)
    make_embedding(embedding_file, embedding, word2idx)

    # split dev into dev and test
    dev_test_examples, _ = process_file(dev_squad)
    # dev_examples, _ = process_txt_files(dev_src_nqg,dev_tgt_nqg,dev_ans_nqg)
    # test_examples, _ = process_txt_files(test_src_nqg, test_tgt_nqg, test_ans_nqg)
    # random.shuffle(dev_test_examples)
    num_dev = len(dev_test_examples) // 2
    dev_examples = dev_test_examples[:num_dev]
    test_examples = dev_test_examples[num_dev:]
    make_conll_format(dev_examples, dev_src_file, dev_trg_file)
    make_conll_format(test_examples, test_src_file, test_trg_file)


if __name__ == "__main__":
    # make_sent_dataset()
    make_para_dataset()

