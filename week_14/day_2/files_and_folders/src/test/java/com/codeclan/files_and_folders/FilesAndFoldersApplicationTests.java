package com.codeclan.files_and_folders;

import com.codeclan.files_and_folders.repositories.FileRepository;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class FilesAndFoldersApplicationTests {

	@Autowired
	FileRepository fileRepository;

	@Test
	void contextLoads() {
	}

}
