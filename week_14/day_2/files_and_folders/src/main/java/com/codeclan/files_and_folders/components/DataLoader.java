package com.codeclan.files_and_folders.components;

import com.codeclan.files_and_folders.models.File;
import com.codeclan.files_and_folders.models.Folder;
import com.codeclan.files_and_folders.models.Person;
import com.codeclan.files_and_folders.repositories.FileRepository;
import com.codeclan.files_and_folders.repositories.FolderRepository;
import com.codeclan.files_and_folders.repositories.PersonRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.context.annotation.Profile;
import org.springframework.stereotype.Component;

@Profile("!test")
//@Component
public class DataLoader implements ApplicationRunner {
    @Autowired
    FileRepository fileRepository;

    @Autowired
    FolderRepository folderRepository;

    @Autowired
    PersonRepository personRepository;

    public DataLoader() {
    }

    public void run(ApplicationArguments args) {
        Person tim = new Person("Tim");
        personRepository.save(tim);

        Person bob = new Person("Bob");
        personRepository.save(bob);

        Folder games = new Folder("Games", tim);
        folderRepository.save(games);

        Folder work = new Folder("Work", bob);
        folderRepository.save(work);

        File tetris = new File("Tetris", ".exe", 16, games);
        fileRepository.save(tetris);

        File frogger = new File("Frogger", ".exe", 20, games);
        fileRepository.save(frogger);

        File cv = new File("CV", ".pdf", 12, work);
        fileRepository.save(cv);

    }
}
