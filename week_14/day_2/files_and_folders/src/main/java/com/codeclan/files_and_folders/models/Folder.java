package com.codeclan.files_and_folders.models;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Entity
@Table(name = "folders")
public class Folder {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long Id;

    @Column(name = "name")
    private String name;

    @JsonIgnoreProperties({"folder"})
    @OneToMany(mappedBy = "folder")
    private List<File> files;

    @ManyToOne
    @JoinColumn(name = "person_id", nullable = false)
    @JsonIgnoreProperties({"folders"})
    private Person person;

    public Folder(String name, Person person) {
        this.name = name;
        this.person = person;
        this.files = new ArrayList<>();
    }

    public Folder() {
    }

    public Long getId() {
        return Id;
    }

    public void setId(Long id) {
        Id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<File> getFiles() {
        return files;
    }

    public void setFiles(List<File> files) {
        this.files = files;
    }

    public void addFile(File file) {
        this.files.add(file);
    }

    public Person getPerson() {
        return person;
    }

    public void setPerson(Person person) {
        this.person = person;
    }
}
