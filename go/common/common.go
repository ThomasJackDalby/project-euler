package common

import (
	"io"
	"strconv"
	"fmt"
	"encoding/hex"
	"crypto/md5"
)

func CheckInt(result int, problem_number int, answer_hash string) {
	hash := md5.New()
	io.WriteString(hash, strconv.Itoa(result))
	expected_hash := hex.EncodeToString(hash.Sum(nil))
	success := expected_hash == answer_hash
	success_text := "Fail"
	if success {
		success_text = "Pass"
	}
	fmt.Printf("Problem %d - %s", problem_number, success_text)
}