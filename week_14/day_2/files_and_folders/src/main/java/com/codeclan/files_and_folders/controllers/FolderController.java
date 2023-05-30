package com.codeclan.files_and_folders.controllers;

import com.codeclan.files_and_folders.models.File;
import com.codeclan.files_and_folders.models.Folder;
import com.codeclan.files_and_folders.repositories.FolderRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
public class FolderController {

    @Autowired
    FolderRepository folderRepository;

    @GetMapping(value = "/folders")
    public ResponseEntity<List<Folder>> getAllFolders() {
        return new ResponseEntity(folderRepository.findAll(), HttpStatus.OK);
    }


    @GetMapping(value = "/folders/{id}")
    public ResponseEntity<Optional<Folder>> getOneFolder(@PathVariable Long id) {
        return new ResponseEntity<>(folderRepository.findById(id), HttpStatus.OK);
    }

    @PostMapping(value = "/folders")
    public ResponseEntity<Folder> createFolder(@RequestBody Folder folder) {
        folderRepository.save(folder);
        return new ResponseEntity<>(folder, HttpStatus.CREATED);
    }

    @DeleteMapping(value = "/folders/{id}")
    public ResponseEntity<Optional> deleteFolder(@PathVariable Long id) {
        folderRepository.deleteById(id);
        return new ResponseEntity<>(HttpStatus.OK);
    }
}
